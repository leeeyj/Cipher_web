from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'home.html')

def caesar(request):
    return render(request, 'caesar.html')

def vigenere_input(request):
    return render(request, 'vigenere_input.html')

def subst_input(request):
    return render(request, 'subst_input.html')

def vigenere_encrypt(request):
    p = request.GET['fulltext_pt']
    p = p.upper()
    k = request.GET['fulltext_key']
    k = k.upper()
    c = ""
    n = len(k)
    for i in range(len(p)):
        a = ord(p[i])
        if a == 32:
            a = 64
        b = ord(k[i%n]) - 64
        t = a + b
        if t > 90:
            t -= 27
        if t == 64:
            t = 32
        c += chr(t)
    return render(request, 'vigenere.html', { 'plaintext': p, 'key': k, 'ciphertext': c })

def subst_encrypt(request):
    Alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    key = 'VWXABCDEIJKFGHLMQRSNOPTUYZ'
    result = ''
    InSet = Alphabet
    OutSet = key
    msg = request.GET['msg']

    for ch in msg:
        if ch.upper() in InSet:
            idx = InSet.find(ch.upper())
            if ch in Alphabet:
                result += OutSet[idx].upper()
            else:
                result += OutSet[idx].lower()
        else:
            result += ch
    return render(request, 'subst.html', {'plaintext':msg, 'ciphertext':result})