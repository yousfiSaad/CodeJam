# https://code.google.com/codejam/contest/2984486/dashboard#s=p0
# yousfi.saad@gmail.com


from sets import Set

def valid(tab, N):
	a = Set()
	b = Set()
	for x in tab:
		a.add(x[0])
		b.add(x[1])
	return N == len(a) and N == len(b)

T = int(stdin.readline())

for t in range(T):
	N, L = (int(e) for e in stdin.readline().split())

	taba = list(int(e, 2) for e in stdin.readline().split())
	tabb = list(int(e, 2) for e in stdin.readline().split())

	ma = {}

	for i in range(N):
		for j in range(N):
			r = taba[i] ^ tabb[j]
			if r in ma:
				ma[r].append((i, j))
			else:
				ma[r] = [(i, j)]

	res = "NOT POSSIBLE"
	for e in sorted(ma, key=lambda keyv: bin(keyv).count("1")):
		if(len(ma[e]) == N):
			if valid(ma[e], N):
				res = str(bin(e).count("1"))
				break

	print("Case #" + str(t+1) + ": " + res)

