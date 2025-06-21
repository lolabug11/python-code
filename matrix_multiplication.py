matrix_width = int(input('What is the side length of your square matrix? '))
if matrix_width == 2:
    ATW = int(input('What is the top right corner of for first 2x2 matrix? '))
    AO = int(input('What is the top left corner of for first 2x2 matrix? '))
    ATH = int(input('What is the bottom left corner of for first 2x2 matrix? '))
    AF = int(input('What is the bottom right corner of for first 2x2 matrix? '))
    BO = int(input('What is the top left corner of for second 2x2 matrix? '))
    BTW = int(input('What is the top right corner of for second 2x2 matrix? '))
    BTH = int(input('What is the bottom left corner of for second 2x2 matrix? '))
    BF = int(input('What is the bottom right corner of for second 2x2 matrix? '))
    CO = AO * BO + ATW * BTH
    CTW = AO * BTW + ATW * BF
    CTH = ATH * BO + AF * BTH
    CF = ATH * BTW + AF * BF
    C = [
        [CO, CTW],
        [CTH, CF]
    ]
    for row in C:
        print(row)
elif matrix_width == 3:
    AO = int(input('What is the top right corner of for first 3x3 matrix? '))
    ATW = int(input('What is the top middle of for first 3x3 matrix? '))
    ATH = int(input('What is the top right corner of for first 3x3 matrix? '))
    AFO = int(input('What is the middle left corner of for first 3x3 matrix? '))
    AFI = int(input('What is the middle middle for first 3x3 matrix? '))
    ASI = int(input('What is the middle right corner of for first 3x3 matrix? '))
    ASE = int(input('What is the bottom left corner of for first 3x3 matrix? '))
    AE = int(input('What is the bottom middle of for first 3x3 matrix? '))
    AN = int(input('What is the bottom right corner of for first 3x3 matrix? '))
    BO = int(input('What is the top left corner of for second 3x3 matrix? '))
    BTW = int(input('What is the top middle of for second 3x3 matrix? '))
    BTH = int(input('What is the top right corner of for second 3x3 matrix? '))
    BFO = int(input('What is the middle left corner of for second 3x3 matrix? '))
    BFI = int(input('What is the middle middle for second 3x3 matrix? '))
    BSI = int(input('What is the middle right corner of for second 3x3 matrix? '))
    BSE = int(input('What is the bottom left corner of for second 3x3 matrix? '))
    BE = int(input('What is the bottom middle of for second 3x3 matrix? '))
    BN = int(input('What is the bottom right corner of for second 3x3 matrix? '))
    a = [AO, ATW, ATH,AFO, AFI, ASI,ASE, AE, AN]
    b = [BO, BTW, BTH, BFO, BFI, BSI, BSE , BE, BN]

    CO = a[0]*b[0]+a[1]*b[3]+a[2]*b[6 ]
    CTW = a[0]*b[1]+a[1]*b[4]+a[2]*b[7]
    CTH = a[0]*b[2]+a[1]*b[5]+a[2]*b[8]
    CFO = a[3]*b[0]+a[4]*b[3]+a[5]*b[6]
    CFI = a[3]*b[1]+a[4]*b[4]+a[5]*b[7]
    CSI = a[3]*b[2]+a[4]*b[5]+a[5]*b[8]
    CSE = a[6]*b[0]+a[7]*b[3]+a[8]*b[6]
    CE = a[6]*b[1]+a[7]*b[4]+a[8]*b[7]
    CN = a[6]*b[2]+a[7]*b[5]+a[8]*b[8]




    C = [
        [CO, CTW, CTH],
        [CFO, CFI, CSI],
        [CSE, CE, CN]
    ]
    for row in C:
        print(row)
