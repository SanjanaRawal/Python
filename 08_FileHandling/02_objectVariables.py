f = open("02_text", mode="r", encoding="utf-8")
print("File name = " , f.name)
print("Encoding = " , f.encoding)
print("Closed = " , f.closed)
print("Mode = " , f.mode)
print("Buffering = " , f.line_buffering)
print("Errors = " , f.errors)
f.close()
print("Closed? " , f.closed)