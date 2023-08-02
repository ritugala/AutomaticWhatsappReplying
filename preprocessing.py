import re
with open('code_removed.txt', encoding="utf-8") as f:
    lines = f.readlines()

ans = []

regex = r"\s?\[\d{1,2}\/\d{1,2}\/\d{2,4}\, \d{1,2}:\d{1,2}:\d{1,2}\s[APM]{2}\]\s"
for line in lines:
	ans.append( re.sub(regex, "", line))
final_ans = ""
for i in range(1, len(ans)):
	ind1 = ans[i].find(':')
	ind2 = ans[i-1].find(':')
	if ans[i][:ind1]==ans[i-1][:ind2]:
		final_ans += ans[i][ind1+1:]
	else:
		final_ans += ans[i]
final_ans = re.sub(r"http\S*", '', final_ans )
final_ans = final_ans.replace("<This message was edited>\n","" )
final_ans = re.sub(r"[^\n]+This message was deleted.\n", '',final_ans) #Also remove the sender of the msg
final_ans = re.sub(r"[^\n]+ omitted\n", '',final_ans) #Also remove the sender of the msg

final_ans = re.sub('Advaith Sridhar', 'Advaith', final_ans)
final_ans = re.sub('Ritu Gala USA', 'User', final_ans)

final_ans
