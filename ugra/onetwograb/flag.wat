(module
  (type $t0 (func (result i32)))
  (type $t1 (func))
  (type $t2 (func (param i32)))
  (type $t3 (func (param i32) (result i32)))
  (func $_initialize (export "_initialize") (type $t1)
    (nop))
  (func $get_flag (export "get_flag") (type $t0) (result i32)
    (local $l0 i32) (local $l1 i32) (local $l2 i32) (local $l3 i32) (local $l4 i32) (local $l5 i32) (local $l6 i32) (local $l7 i64) (local $l8 i64)
    (local.set $l1
      (i32.add
        (global.get $g0)
        (i32.const -64)))
    (i32.store
      (i32.const 1112)
      (i32.const 1097790850))
    (i64.store
      (i32.const 1104)
      (i64.const -6685739018505682416))
    (local.set $l0
      (i32.const 3))
    (local.set $l2
      (i32.const 83886608))
    (loop $L0
      (i32.store
        (i32.add
          (local.tee $l3
            (i32.shl
              (local.get $l0)
              (i32.const 2)))
          (i32.const 1104))
        (i32.xor
          (i32.xor
            (local.tee $l5
              (i32.load
                (i32.add
                  (local.get $l3)
                  (i32.const 1096))))
            (i32.xor
              (local.get $l0)
              (local.get $l2)))
          (i32.const -1640531527)))
      (if $I1
        (i32.eqz
          (i32.eq
            (local.tee $l4
              (i32.add
                (local.get $l0)
                (i32.const 1)))
            (i32.const 4096)))
        (then
          (i32.store
            (i32.add
              (i32.shl
                (local.get $l4)
                (i32.const 2))
              (i32.const 1104))
            (i32.xor
              (i32.xor
                (local.tee $l2
                  (i32.load
                    (i32.add
                      (local.get $l3)
                      (i32.const 1100))))
                (i32.xor
                  (local.get $l4)
                  (local.get $l5)))
              (i32.const -1640531527)))
          (local.set $l0
            (i32.add
              (local.get $l0)
              (i32.const 2)))
          (br $L0))))
    (i64.store offset=56
      (local.get $l1)
      (i64.const -4775302468169978968))
    (i64.store offset=48
      (local.get $l1)
      (i64.const -6511466616283819120))
    (i64.store offset=40
      (local.get $l1)
      (i64.const -8247630764397659272))
    (i64.store offset=32
      (local.get $l1)
      (i64.const 8462949161198052192))
    (i64.store offset=24
      (local.get $l1)
      (i64.const 6726785013084212040))
    (i64.store offset=16
      (local.get $l1)
      (i64.const 4990620864970371888))
    (i64.store offset=8
      (local.get $l1)
      (i64.const 3254456716856531736))
    (i64.store
      (local.get $l1)
      (i64.const 1518292568742691584))
    (local.set $l0
      (i32.load
        (i32.const 1096)))
    (local.set $l3
      (i32.load
        (i32.const 1092)))
    (local.set $l2
      (i32.const 0))
    (loop $L2
      (i32.store
        (local.tee $l4
          (i32.add
            (i32.shl
              (local.tee $l3
                (i32.and
                  (i32.add
                    (local.get $l3)
                    (i32.const 1))
                  (i32.const 4095)))
              (i32.const 2))
            (i32.const 1104)))
        (local.tee $l0
          (i32.sub
            (i32.sub
              (select
                (i32.const -1)
                (i32.const 0)
                (local.tee $l5
                  (i32.lt_u
                    (local.tee $l0
                      (i32.wrap_i64
                        (i64.add
                          (local.tee $l8
                            (i64.shr_u
                              (local.tee $l7
                                (i64.add
                                  (i64.extend_i32_u
                                    (local.get $l0))
                                  (i64.mul
                                    (i64.load32_u
                                      (local.get $l4))
                                    (i64.const 18782))))
                              (i64.const 32)))
                          (local.get $l7))))
                    (local.tee $l4
                      (i32.wrap_i64
                        (local.get $l8))))))
              (local.get $l0))
            (i32.const 2))))
      (i32.store8
        (local.tee $l6
          (i32.add
            (local.get $l1)
            (i32.and
              (i32.shr_u
                (local.get $l0)
                (i32.const 16))
              (i32.const 63))))
        (i32.xor
          (i32.load8_u
            (local.get $l6))
          (local.get $l0)))
      (local.set $l0
        (i32.add
          (local.get $l4)
          (local.get $l5)))
      (br_if $L2
        (i32.ne
          (local.tee $l2
            (i32.add
              (local.get $l2)
              (i32.const 1)))
          (i32.const -1))))
    (i32.store
      (i32.const 1096)
      (local.get $l0))
    (i32.store
      (i32.const 1092)
      (local.get $l3))
    (local.set $l0
      (i32.const 0))
    (loop $L3
      (i32.store8
        (local.tee $l2
          (i32.add
            (i32.load
              (i32.const 1100))
            (local.get $l0)))
        (i32.xor
          (i32.load8_u
            (i32.add
              (local.get $l0)
              (local.get $l1)))
          (i32.load8_u
            (local.get $l2))))
      (i32.store8
        (local.tee $l3
          (i32.add
            (local.tee $l2
              (i32.or
                (local.get $l0)
                (i32.const 1)))
            (i32.load
              (i32.const 1100))))
        (i32.xor
          (i32.load8_u
            (i32.add
              (local.get $l1)
              (local.get $l2)))
          (i32.load8_u
            (local.get $l3))))
      (br_if $L3
        (i32.ne
          (local.tee $l0
            (i32.add
              (local.get $l0)
              (i32.const 2)))
          (i32.const 64))))
    (i32.load
      (i32.const 1100)))
  (func $get_flag_length (export "get_flag_length") (type $t0) (result i32)
    (i32.const 64))
  (func $stackSave (export "stackSave") (type $t0) (result i32)
    (global.get $g0))
  (func $stackRestore (export "stackRestore") (type $t2) (param $p0 i32)
    (global.set $g0
      (local.get $p0)))
  (func $stackAlloc (export "stackAlloc") (type $t3) (param $p0 i32) (result i32)
    (global.set $g0
      (local.tee $p0
        (i32.and
          (i32.sub
            (global.get $g0)
            (local.get $p0))
          (i32.const -16))))
    (local.get $p0))
  (func $__errno_location (export "__errno_location") (type $t0) (result i32)
    (i32.const 17488))
  (table $__indirect_function_table (export "__indirect_function_table") 2 2 funcref)
  (memory $memory (export "memory") 256 256)
  (global $g0 (mut i32) (i32.const 5260384))
  (elem $e0 (i32.const 1) func $_initialize)
  (data $d0 (i32.const 1024) "k\eeuR\d4\09\c7\f9(\17\cf\eb\ee\1dG\1bX\8av\b4)\ac\e4\1c1\98\b2f\a21*\8d5\05\fd\0c\ad\1a\e79xdb\03\87\bfw\d1\9f\90X~I\cf\80rG\a7\09\1b\d6!\ba2")
  (data $d1 (i32.const 1092) "\ff\0f\00\00\c4\87\05\00\00\04"))