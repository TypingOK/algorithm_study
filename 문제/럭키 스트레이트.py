N = input()

mid = len(N)//2
start = list(map(int, N[:mid]))
end = list(map(int, N[mid:]))

if sum(start) == sum(end):
    print("LUCKY")
else:
    print("READY")
