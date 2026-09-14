# w15-03-en-uzun-satir.py — dosyadaki en uzun satırı ve numarasını bulma

longest = ""
longest_no = 0
with open("siir.txt", encoding="utf-8") as f:
    for number, line in enumerate(f, start=1):
        line = line.strip()          # \n uzunluğa katılmasın
        if len(line) > len(longest):
            longest = line
            longest_no = number

print(f"En uzun satır {longest_no}. satır ({len(longest)} karakter):")
print(longest)
