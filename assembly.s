.global _start
 _start:
    ldr r0, =n0
    vldr.f64 d0, [r0]
    vpush.f64 {d0}
    vpop.f64 {d0}
    ldr r0, =PI
    vstr.f64 d0, [r0]
    vpush.f64 {d0}
    vpop.f64 {d0}
    ldr r0, =r_0
    vstr.f64 d0, [r0]
    ldr r0, =n1
    vldr.f64 d0, [r0]
    vpush.f64 {d0}
    ldr r0, =PI
    vldr.f64 d0, [r0]
    vpush.f64 {d0}
    vpop.f64 {d1}
    vpop.f64 {d0}
    vmul.f64 d2, d0, d1
    vpush.f64 {d2}
    vpop.f64 {d0}
    ldr r0, =r_1
    vstr.f64 d0, [r0]
    ldr r0, =n2
    vldr.f64 d0, [r0]
    vpush.f64 {d0}
    vpop.f64 {d0}
    ldr r0, =VALOR
    vstr.f64 d0, [r0]
    vpush.f64 {d0}
    vpop.f64 {d0}
    ldr r0, =r_2
    vstr.f64 d0, [r0]
    ldr r0, =VALOR
    vldr.f64 d0, [r0]
    vpush.f64 {d0}
    ldr r0, =PI
    vldr.f64 d0, [r0]
    vpush.f64 {d0}
    vpop.f64 {d1}
    vpop.f64 {d0}
    vdiv.f64 d2, d0, d1
    vpush.f64 {d2}
    vpop.f64 {d0}
    ldr r0, =r_3
    vstr.f64 d0, [r0]
    ldr r0, =n3
    vldr.f64 d0, [r0]
    vpush.f64 {d0}
    ldr r0, =n4
    vldr.f64 d0, [r0]
    vpush.f64 {d0}
    vpop.f64 {d1}
    vpop.f64 {d0}
    vadd.f64 d2, d0, d1
    vpush.f64 {d2}
    vpop.f64 {d0}
    ldr r0, =X
    vstr.f64 d0, [r0]
    vpush.f64 {d0}
    ldr r0, =X
    vldr.f64 d0, [r0]
    vpush.f64 {d0}
    vpop.f64 {d1}
    vpop.f64 {d0}
    vmul.f64 d2, d0, d1
    vpush.f64 {d2}
    vpop.f64 {d0}
    ldr r0, =r_4
    vstr.f64 d0, [r0]
    ldr r0, =n5
    vldr.f64 d0, [r0]
    vpush.f64 {d0}
    vpop.f64 {d0}
    vcvt.s32.f64 s0, d0
    vmov r1, s0
    ldr r0, =r_0
    lsl r1, r1, #3
    add r0, r0, r1
    vldr.f64 d0, [r0]
    vpush.f64 {d0}
    vpop.f64 {d0}
    ldr r0, =r_5
    vstr.f64 d0, [r0]
    ldr r0, =n6
    vldr.f64 d0, [r0]
    vpush.f64 {d0}
    vpop.f64 {d0}
    vcvt.s32.f64 s0, d0
    vmov r1, s0
    ldr r0, =r_0
    lsl r1, r1, #3
    add r0, r0, r1
    vldr.f64 d0, [r0]
    vpush.f64 {d0}
    ldr r0, =n7
    vldr.f64 d0, [r0]
    vpush.f64 {d0}
    vpop.f64 {d1}
    vpop.f64 {d0}
    vadd.f64 d2, d0, d1
    vpush.f64 {d2}
    vpop.f64 {d0}
    ldr r0, =r_6
    vstr.f64 d0, [r0]
    ldr r0, =n8
    vldr.f64 d0, [r0]
    vpush.f64 {d0}
    vpop.f64 {d0}
    vcvt.s32.f64 s0, d0
    vmov r1, s0
    ldr r0, =r_0
    lsl r1, r1, #3
    add r0, r0, r1
    vldr.f64 d0, [r0]
    vpush.f64 {d0}
    ldr r0, =n9
    vldr.f64 d0, [r0]
    vpush.f64 {d0}
    vpop.f64 {d0}
    vcvt.s32.f64 s0, d0
    vmov r1, s0
    ldr r0, =r_0
    lsl r1, r1, #3
    add r0, r0, r1
    vldr.f64 d0, [r0]
    vpush.f64 {d0}
    vpop.f64 {d1}
    vpop.f64 {d0}
    vmul.f64 d2, d0, d1
    vpush.f64 {d2}
    vpop.f64 {d0}
    ldr r0, =r_7
    vstr.f64 d0, [r0]
    ldr r0, =n10
    vldr.f64 d0, [r0]
    vpush.f64 {d0}
    ldr r0, =n11
    vldr.f64 d0, [r0]
    vpush.f64 {d0}
    vpop.f64 {d0}
    vcvt.s32.f64 s0, d0
    vmov r1, s0
    ldr r0, =r_0
    lsl r1, r1, #3
    add r0, r0, r1
    vldr.f64 d0, [r0]
    vpush.f64 {d0}
    vpop.f64 {d1}
    vpop.f64 {d0}
    vadd.f64 d2, d0, d1
    vpush.f64 {d2}
    ldr r0, =n12
    vldr.f64 d0, [r0]
    vpush.f64 {d0}
    vpop.f64 {d0}
    vcvt.s32.f64 s0, d0
    vmov r1, s0
    ldr r0, =r_0
    lsl r1, r1, #3
    add r0, r0, r1
    vldr.f64 d0, [r0]
    vpush.f64 {d0}
    vpop.f64 {d1}
    vpop.f64 {d0}
    vdiv.f64 d2, d0, d1
    vpush.f64 {d2}
    vpop.f64 {d0}
    ldr r0, =r_8
    vstr.f64 d0, [r0]
    ldr r0, =n13
    vldr.f64 d0, [r0]
    vpush.f64 {d0}
    vpop.f64 {d0}
    vcvt.s32.f64 s0, d0
    vmov r1, s0
    ldr r0, =r_0
    lsl r1, r1, #3
    add r0, r0, r1
    vldr.f64 d0, [r0]
    vpush.f64 {d0}
    ldr r0, =n14
    vldr.f64 d0, [r0]
    vpush.f64 {d0}
    vpop.f64 {d1}
    vpop.f64 {d0}
    vcvt.s32.f64 s2, d1
    vmov r2, s2
    ldr r0, =const_um
    vldr.f64 d2, [r0]
    cmp r2, #0
    beq .fim_pot0
.pot0:
    cmp r2, #0
    ble .fim_pot0
    vmul.f64 d2, d2, d0
    sub r2, r2, #1
    b .pot0
.fim_pot0:
    vpush.f64 {d2}
    vpop.f64 {d0}
    ldr r0, =r_9
    vstr.f64 d0, [r0]
.data
    const_um: .double 1.0
    n0: .double 3.14159
    PI: .double 0.0
    n1: .double 10.0
    n2: .double 50.0
    VALOR: .double 0.0
    n3: .double 10.0
    n4: .double 2.0
    X: .double 0.0
    n5: .double 1
    n6: .double 2
    n7: .double 10.0
    n8: .double 1
    n9: .double 3
    n10: .double 5.0
    n11: .double 1
    n12: .double 2
    n13: .double 1
    n14: .double 2.0
    r_0: .double 0.0
    r_1: .double 0.0
    r_2: .double 0.0
    r_3: .double 0.0
    r_4: .double 0.0
    r_5: .double 0.0
    r_6: .double 0.0
    r_7: .double 0.0
    r_8: .double 0.0
    r_9: .double 0.0
