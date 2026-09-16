import term
def vbb(ffv,ssd):
    try: 
        ffv=int(ffv)
        if ffv in ssd:
            return ffv
        else: 
            term.writeLine('неправильный ввод',term.red)
            ggg=input().strip()
            return vbb(ggg,ssd)
    except:
        term.writeLine('ошибка',term.red)
        ccc=input().strip()
        return vbb(ccc,ssd)

