'''
用safe_float()来处理信用卡交易文件，将其作为字符串读入。并用一个日志文件跟踪处理进程。
'''

def safe_float(obj):
    'safe version of float()'
    try:
        retval = float(obj)
    except(ValueError,TypeError) as diag:
        retval = str(diag)
    return retval

def main():
    'handles all the data processing'
    log = open('cardlog.txt','w')
    try:
        ccfile = open('carddata.txt','r')
    except IOError as e:
        log.write('no txns this month\n')
        log.close()
        return
    txns = ccfile.readlines()
    ccfile.close()
    total = 0.00
    log.write('account log:\n')

    for eachTxn in txns:
        result = safe_float(eachTxn)
        if isinstance(result,float):  #判断是否是float类型
            total += result
            log.write('data...processed\n')
        else:
            log.write('ignored: %s\n' %result)
    print('$%.2f(new balance)' % total)
    log.close()

if __name__=='__main__':
    main()
