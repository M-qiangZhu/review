from pyzx测试demo import 生成器 as scq
st = scq.steiner_g()

# debug = False
debug = True

if debug:
    print(next(st))
    debug = not debug
