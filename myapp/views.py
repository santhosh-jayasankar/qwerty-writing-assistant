from django.shortcuts import render, redirect
from django.contrib.auth import login as auth_login, authenticate
from .forms import SignupForm
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import logout
import requests
from googletrans import Translator
from django.conf import settings
from .models import ToolHistory
import language_tool_python

# Create your views here.

def home(request):
    return render(request,'home.html')

def grammertool(request):
    return render(request,'grammertool.html')

def translationtool(request):
    return render(request,"translate.html")

def rephrasetool(request):
    return render(request,"rephrasetool.html")

def about(request):
    return render(request,"about.html")

def profile(request):

    history_qs = ToolHistory.objects.filter(
        user=request.user
    ).order_by("-created_at")

    history = []
    for h in history_qs:
        history.append({
            "tool": h.tool,
            "input": h.input_text,
            "output": h.output_text
        })

    return render(request, "profile.html", {
        "history": history
    })

def login_page(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)

        if user is not None:
            auth_login(request, user)
            return redirect("profile")
        else:
            messages.error(request, "Invalid username or password")

    return render(request, "login.html")



def signup_page(request):
    if request.method=="POST":
        form=SignupForm(request.POST)
        print(form.errors)
        if form.is_valid():
            user=form.save()
            auth_login(request,user)
            return redirect("home")
    else:
        form=SignupForm()
    return render(request,"signup.html",{'form':form})


def logout_view(request):
    logout(request)
    return redirect('home')

tool = language_tool_python.LanguageTool('en-US',remote_server='https://api.languagetool.org')

def grammar_fix(request):
    input_text = request.POST.get("input_text", "").strip()
    corrected_text = input_text

    if input_text:
        try:
            matches = tool.check(input_text)
            corrected_text = language_tool_python.utils.correct(
                input_text, matches
            )
        except Exception as e:
            print("LanguageTool public server error:", e)
            corrected_text = input_text

    if request.method == "POST" and input_text and request.user.is_authenticated:
        ToolHistory.objects.create(
            user=request.user,
            tool="Grammar Correction",
            input_text=input_text,
            output_text=corrected_text
        )

    return render(request, "grammertool.html", {
        "input_text": input_text,
        "output_text": corrected_text
    })

translator = Translator()

def translate_fix(request):
    input_text = request.POST.get("input_text", "").strip()
    output_text = ""

    src = request.POST.get("src", "en")
    dest = request.POST.get("dest", "ta")

    if input_text:
        try:
            result = translator.translate(input_text, src=src, dest=dest)
            output_text = result.text
        except Exception as e:
            print("Translation error:", e)
            output_text = "Translation temporarily unavailable."

    if request.method == "POST" and input_text and request.user.is_authenticated:
        ToolHistory.objects.create(
            user=request.user,
            tool="Translation",
            input_text=input_text,
            output_text=output_text
        )

    return render(request, "translate.html", {
        "input_text": input_text,
        "output_text": output_text,
        "src": src,
        "dest": dest
    })

def rephraser(request):
    if request.method != "POST":
        return redirect("rephrasetool")

    input_text = request.POST.get("input_text", "").strip()
    output_text = ""

    if not input_text:
        return render(request, "rephrasetool.html", {
            "input_text": "",
            "output_text": ""
        })

    try:
        url = "https://api.sapling.ai/api/v1/paraphrase"

        payload = {
            "key": settings.SAPLING_API_KEY,
            "text": input_text,
        }

        response = requests.post(url, json=payload, timeout=20)

        if response.status_code == 200:
            data = response.json()
            results = data.get("results", [])

            if results:

                lines = []
                for i, r in enumerate(results[:5], start=1):
                    lines.append(f"{i}. {r.get('replacement', '')}")

                output_text = "\n".join(lines)
            else:
                output_text = "No rephrased sentences generated."

        else:
            print("Sapling error:", response.status_code, response.text)
            output_text = "Rephrase service temporarily unavailable."

    except Exception as e:
        print("Sapling exception:", e)
        output_text = "Error connecting to rephrase service."

    if request.user.is_authenticated and input_text:
        ToolHistory.objects.create(
            user=request.user,
            tool="Rephraser",
            input_text=input_text,
            output_text=output_text
        )

    return render(request, "rephrasetool.html", {
        "input_text": input_text,
        "output_text": output_text
    })
