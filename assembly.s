.global _start
 _start:
    ldr r0, =n0
    vldr.f64 d0, [r0]
    vpush.f64 {d0}
    ldr r0, =n1
    vldr.f64 d0, [r0]
    vpush.f64 {d0}
    vpop.f64 {d1}
    vpop.f64 {d0}
    vadd.f64 d2, d0, d1
    vpush.f64 {d2}
    vpop.f64 {d0}
    ldr r0, =MEM
    vstr.f64 d0, [r0]
    vpush.f64 {d0}
    vpop.f64 {d0}
    ldr r0, =r_0
    vstr.f64 d0, [r0]
    ldr r0, =MEM
    vldr.f64 d0, [r0]
    vpush.f64 {d0}
    ldr r0, =n2
    vldr.f64 d0, [r0]
    vpush.f64 {d0}
    ldr r0, =n3
    vldr.f64 d0, [r0]
    vpush.f64 {d0}
    vpop.f64 {d1}
    vpop.f64 {d0}
    vdiv.f64 d2, d0, d1
    vpush.f64 {d2}
    vpop.f64 {d1}
    vpop.f64 {d0}
    vmul.f64 d2, d0, d1
    vpush.f64 {d2}
    vpop.f64 {d0}
    ldr r0, =X
    vstr.f64 d0, [r0]
    vpush.f64 {d0}
    vpop.f64 {d0}
    ldr r0, =r_1
    vstr.f64 d0, [r0]
    ldr r0, =n4
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
    ldr r0, =X
    vldr.f64 d0, [r0]
    vpush.f64 {d0}
    vpop.f64 {d1}
    vpop.f64 {d0}
    vadd.f64 d2, d0, d1
    vpush.f64 {d2}
    vpop.f64 {d0}
    ldr r0, =r_2
    vstr.f64 d0, [r0]
    ldr r0, =n5
    vldr.f64 d0, [r0]
    vpush.f64 {d0}
    vpop.f64 {d0}
    ldr r0, =Y
    vstr.f64 d0, [r0]
    vpush.f64 {d0}
    ldr r0, =n6
    vldr.f64 d0, [r0]
    vpush.f64 {d0}
    vpop.f64 {d1}
    vpop.f64 {d0}
    vadd.f64 d2, d0, d1
    vpush.f64 {d2}
    ldr r0, =n7
    vldr.f64 d0, [r0]
    vpush.f64 {d0}
    ldr r0, =n8
    vldr.f64 d0, [r0]
    vpush.f64 {d0}
    vpop.f64 {d1}
    vpop.f64 {d0}
    vadd.f64 d2, d0, d1
    vpush.f64 {d2}
    vpop.f64 {d1}
    vpop.f64 {d0}
    vadd.f64 d2, d0, d1
    vpush.f64 {d2}
    vpop.f64 {d0}
    ldr r0, =r_3
    vstr.f64 d0, [r0]
    ldr r0, =n9
    vldr.f64 d0, [r0]
    vpush.f64 {d0}
    ldr r0, =n10
    vldr.f64 d0, [r0]
    vpush.f64 {d0}
    vpop.f64 {d1}
    vpop.f64 {d0}
    vadd.f64 d2, d0, d1
    vpush.f64 {d2}
    ldr r0, =Y
    vldr.f64 d0, [r0]
    vpush.f64 {d0}
    vpop.f64 {d1}
    vpop.f64 {d0}
    vadd.f64 d2, d0, d1
    vpush.f64 {d2}
    ldr r0, =n11
    vldr.f64 d0, [r0]
    vpush.f64 {d0}
    ldr r0, =n12
    vldr.f64 d0, [r0]
    vpush.f64 {d0}
    vpop.f64 {d1}
    vpop.f64 {d0}
    vadd.f64 d2, d0, d1
    vpush.f64 {d2}
    vpop.f64 {d1}
    vpop.f64 {d0}
    vadd.f64 d2, d0, d1
    vpush.f64 {d2}
    vpop.f64 {d0}
    ldr r0, =r_4
    vstr.f64 d0, [r0]
    ldr r0, =Y
    vldr.f64 d0, [r0]
    vpush.f64 {d0}
    ldr r0, =n13
    vldr.f64 d0, [r0]
    vpush.f64 {d0}
    ldr r0, =n14
    vldr.f64 d0, [r0]
    vpush.f64 {d0}
    vpop.f64 {d1}
    vpop.f64 {d0}
    vadd.f64 d2, d0, d1
    vpush.f64 {d2}
    vpop.f64 {d1}
    vpop.f64 {d0}
    vadd.f64 d2, d0, d1
    vpush.f64 {d2}
    vpop.f64 {d0}
    ldr r0, =r_5
    vstr.f64 d0, [r0]
    ldr r0, =n15
    vldr.f64 d0, [r0]
    vpush.f64 {d0}
    ldr r0, =n16
    vldr.f64 d0, [r0]
    vpush.f64 {d0}
    vpop.f64 {d1}
    vpop.f64 {d0}
    vadd.f64 d2, d0, d1
    vpush.f64 {d2}
    vpop.f64 {d0}
    ldr r0, =r_6
    vstr.f64 d0, [r0]
    ldr r0, =n17
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
    ldr r0, =r_7
    vstr.f64 d0, [r0]
    ldr r0, =n18
    vldr.f64 d0, [r0]
    vpush.f64 {d0}
    ldr r0, =n19
    vldr.f64 d0, [r0]
    vpush.f64 {d0}
    vpop.f64 {d1}
    vpop.f64 {d0}
    vmul.f64 d2, d0, d1
    vpush.f64 {d2}
    ldr r0, =n20
    vldr.f64 d0, [r0]
    vpush.f64 {d0}
    ldr r0, =n21
    vldr.f64 d0, [r0]
    vpush.f64 {d0}
    vpop.f64 {d1}
    vpop.f64 {d0}
    vmul.f64 d2, d0, d1
    vpush.f64 {d2}
    vpop.f64 {d1}
    vpop.f64 {d0}
    vdiv.f64 d2, d0, d1
    vpush.f64 {d2}
    vpop.f64 {d0}
    ldr r0, =r_8
    vstr.f64 d0, [r0]
    ldr r0, =n22
    vldr.f64 d0, [r0]
    vpush.f64 {d0}
    vpop.f64 {d0}
    ldr r0, =MEM
    vstr.f64 d0, [r0]
    vpush.f64 {d0}
    vpop.f64 {d0}
    ldr r0, =r_9
    vstr.f64 d0, [r0]
.data
    const_um: .double 1.0
    n0: .double 1
    n1: .double 2
    MEM: .double 0.0
    n2: .double 1
    n3: .double 2
    X: .double 0.0
    n4: .double 1
    n5: .double 2
    Y: .double 0.0
    n6: .double 3
    n7: .double 2
    n8: .double 1
    n9: .double 2
    n10: .double 3
    n11: .double 2
    n12: .double 1
    n13: .double 2
    n14: .double 1
    n15: .double 3.14
    n16: .double 2.0
    n17: .double 3
    n18: .double 1.5
    n19: .double 2.0
    n20: .double 3.0
    n21: .double 4.0
    n22: .double 5.0
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
