# QiuChenly 计算数据差值做特征码算法
# 部分网友提供了原始版本 虽然是用的Chatgpt写给我的 但是还是略表谢意
# 提供不定长度的多个十六进制汇编代码段 自动求出差值特征码

data = '''
55 48 89 E5 48 81 EC A0 06 00 00 48 8B 05 C6 3E 27 00 48 8B 00 48 89 45 F8 48 89 BD 18 FD FF FF C6 85 17 FD FF FF 00 E8 4E 75 16 00 48 8B 0D 35 3B 27 00 48 C7 85 08 FD FF FF 00 00 00 00 48 8B 95 08 FD FF FF 48 89 95 00 FD FF FF 48 8D 95 00 FD FF FF 48 89 95 60 FD FF FF 48 83 39 00 48 89 85 E8 FC FF FF 0F 84 39 00 00 00 48 8B 05 D6 19 41 00 48 8B 0D EF 3A 27 00 48 8B 39 48 8D 35 1D 1A 41 00 FF D0 48 89 85 E0 FC FF FF E9 00 00 00 00 48 8B 85 E0 FC FF FF 48 89 85 D8 FC FF FF E9 10 00 00 00 31 C0 89 C1 48 89 8D D8 FC FF FF E9 00 00 00 00 48 8B 85 D8 FC FF FF 48 89 85 58 FD FF FF 48 8B 95 58 FD FF FF 48 8D 3D 86 F1 1A 00 48 8D 35 29 F1 29 00 31 C9 88 C8 E8 B0 DF 05 00 E9 00 00 00 00 48 83 BD 58 FD FF FF 00

55 48 89 E5 48 81 EC A0 06 00 00 48 8B 05 56 E4 26 00 48 8B 00 48 89 45 F8 48 89 BD 18 FD FF FF C6 85 17 FD FF FF 00 E8 4E 75 16 00 48 8B 0D 35 3B 27 00 48 C7 85 08 FD FF FF 00 00 00 00 48 8B 95 08 FD FF FF 48 89 95 00 FD FF FF 48 8D 95 00 FD FF FF 48 89 95 60 FD FF FF 48 83 39 00 48 89 85 E8 FC FF FF 0F 84 39 00 00 00 48 8B 05 D6 19 41 00 48 8B 0D EF 3A 27 00 48 8B 39 48 8D 35 1D 1A 41 00 FF D0 48 89 85 E0 FC FF FF E9 00 00 00 00 48 8B 85 E0 FC FF FF 48 89 85 D8 FC FF FF E9 10 00 00 00 31 C0 89 C1 48 89 8D D8 FC FF FF E9 00 00 00 00 48 8B 85 D8 FC FF FF 48 89 85 58 FD FF FF 48 8B 95 58 FD FF FF 48 8D 3D 86 F1 1A 00 48 8D 35 29 F1 29 00 31 C9 88 C8 E8 B0 DF 05 00 E9 00 00 00 00 48 83 BD 58 FD FF FF 00
'''

data1 = []

for i in data.split("\n"):
    if i == '':
        continue
    else:
        data1.append(i)
        if len(data1) > 1:
            res = " ".join([
                d1 if d1 == d2 else "??" for d1, d2 in zip(data1[0].split(), data1[1].split())
            ])
            data1 = [res]

print(data1[0])