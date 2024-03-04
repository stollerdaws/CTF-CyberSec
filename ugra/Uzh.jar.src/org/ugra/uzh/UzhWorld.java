package org.ugra.uzh;

import java.util.Random;

public class UzhWorld {
  public static final byte CELLS_X = 40;
  
  public static final byte CELLS_Y = 30;
  
  public static final int FRUIT_STEP_DELAY_SCALE = 1000;
  
  public static final int FRUIT_STEP_DELAY_K = 3000;
  
  private Random a;
  
  private UzhBody a;
  
  private Point a;
  
  private boolean a;
  
  private int a = 0;
  
  private int b;
  
  public UzhWorld(long paramLong, byte paramByte) {
    this.a = 400;
    this.b = 0;
    this.a = new Random(paramLong);
    Point point = new Point((byte)20, (byte)15);
    this.a = new UzhBody(point, paramByte, (byte)5);
    a();
  }
  
  public UzhBody getBody() {
    return this.a;
  }
  
  public Point getFruit() {
    return this.a;
  }
  
  public int getStepDelay() {
    return this.a;
  }
  
  public int getEatenFruits() {
    return this.b;
  }
  
  public boolean advance(byte paramByte) {
    // Byte code:
    //   0: aload_0
    //   1: getfield a : Lorg/ugra/uzh/UzhBody;
    //   4: iload_1
    //   5: invokevirtual advanceHead : (B)V
    //   8: aload_0
    //   9: getfield a : Z
    //   12: ifeq -> 23
    //   15: aload_0
    //   16: iconst_0
    //   17: putfield a : Z
    //   20: goto -> 30
    //   23: aload_0
    //   24: getfield a : Lorg/ugra/uzh/UzhBody;
    //   27: invokevirtual shrinkTail : ()V
    //   30: aload_0
    //   31: getfield a : Lorg/ugra/uzh/UzhBody;
    //   34: invokevirtual getHeadSegment : ()Lorg/ugra/uzh/UzhBody$Segment;
    //   37: getfield head : Lorg/ugra/uzh/Point;
    //   40: astore_1
    //   41: aload_0
    //   42: getfield a : Lorg/ugra/uzh/UzhBody;
    //   45: invokevirtual headIntersects : ()Z
    //   48: ifne -> 83
    //   51: aload_1
    //   52: getfield x : B
    //   55: iflt -> 83
    //   58: aload_1
    //   59: getfield y : B
    //   62: iflt -> 83
    //   65: aload_1
    //   66: getfield x : B
    //   69: bipush #40
    //   71: if_icmpge -> 83
    //   74: aload_1
    //   75: getfield y : B
    //   78: bipush #30
    //   80: if_icmplt -> 85
    //   83: iconst_0
    //   84: ireturn
    //   85: aload_0
    //   86: getfield a : Lorg/ugra/uzh/Point;
    //   89: aload_0
    //   90: getfield a : Lorg/ugra/uzh/UzhBody;
    //   93: invokevirtual getHeadSegment : ()Lorg/ugra/uzh/UzhBody$Segment;
    //   96: getfield head : Lorg/ugra/uzh/Point;
    //   99: invokevirtual equals : (Ljava/lang/Object;)Z
    //   102: ifeq -> 140
    //   105: aload_0
    //   106: iconst_1
    //   107: putfield a : Z
    //   110: aload_0
    //   111: invokespecial a : ()V
    //   114: aload_0
    //   115: aload_0
    //   116: getfield a : I
    //   119: sipush #1000
    //   122: imul
    //   123: sipush #3000
    //   126: idiv
    //   127: putfield a : I
    //   130: aload_0
    //   131: dup
    //   132: getfield b : I
    //   135: iconst_1
    //   136: iadd
    //   137: putfield b : I
    //   140: iconst_1
    //   141: ireturn
  }
  
  private void a() {
    // Byte code:
    //   0: aload_0
    //   1: new org/ugra/uzh/Point
    //   4: dup
    //   5: aload_0
    //   6: getfield a : Ljava/util/Random;
    //   9: invokevirtual nextInt : ()I
    //   12: invokestatic abs : (I)I
    //   15: bipush #40
    //   17: irem
    //   18: i2b
    //   19: aload_0
    //   20: getfield a : Ljava/util/Random;
    //   23: invokevirtual nextInt : ()I
    //   26: invokestatic abs : (I)I
    //   29: bipush #30
    //   31: irem
    //   32: i2b
    //   33: invokespecial <init> : (BB)V
    //   36: putfield a : Lorg/ugra/uzh/Point;
    //   39: aload_0
    //   40: getfield a : Lorg/ugra/uzh/UzhBody;
    //   43: aload_0
    //   44: getfield a : Lorg/ugra/uzh/Point;
    //   47: invokevirtual pointIntersects : (Lorg/ugra/uzh/Point;)Z
    //   50: ifne -> 0
    //   53: return
  }
}


/* Location:              /home/ubuntusfs/Downloads/Uzh.jar!/org/ugra/uzh/UzhWorld.class
 * Java compiler version: 3 (47.0)
 * JD-Core Version:       1.1.3
 */