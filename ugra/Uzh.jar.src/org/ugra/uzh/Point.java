package org.ugra.uzh;

public class Point {
  public static final byte LEFT = -1;
  
  public static final byte RIGHT = 1;
  
  public static final byte UP = -2;
  
  public static final byte DOWN = 2;
  
  public byte x;
  
  public byte y;
  
  public Point(byte paramByte1, byte paramByte2) {
    this.x = paramByte1;
    this.y = paramByte2;
  }
  
  public Point(Point paramPoint) {
    this.x = paramPoint.x;
    this.y = paramPoint.y;
  }
  
  final void a(byte paramByte1, byte paramByte2) {
    switch (paramByte1) {
      case -1:
        this.x = (byte)(this.x - paramByte2);
        return;
      case 1:
        this.x = (byte)(this.x + paramByte2);
        return;
      case 2:
        this.y = (byte)(this.y - paramByte2);
        return;
      case -2:
        this.y = (byte)(this.y + paramByte2);
        return;
    } 
    throw new RuntimeException("Invalid direction");
  }
  
  public boolean equals(Object paramObject) {
    if (!(paramObject instanceof Point))
      return false; 
    paramObject = paramObject;
    return (this.x == ((Point)paramObject).x && this.y == ((Point)paramObject).y);
  }
  
  public String toString() {
    return "(" + String.valueOf(this.x) + ", " + String.valueOf(this.y) + ")";
  }
  
  public static String directionToString(byte paramByte) {
    switch (paramByte) {
      case 2:
        return "DOWN";
      case -2:
        return "UP";
      case -1:
        return "LEFT";
      case 1:
        return "RIGHT";
    } 
    throw new RuntimeException("Invalid direction");
  }
  
  public static byte invertDirection(byte paramByte) {
    return (byte)-paramByte;
  }
}


/* Location:              /home/ubuntusfs/Downloads/Uzh.jar!/org/ugra/uzh/Point.class
 * Java compiler version: 3 (47.0)
 * JD-Core Version:       1.1.3
 */