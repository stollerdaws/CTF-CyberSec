package org.ugra.uzh;

public class UzhBody$Segment {
  public Point head;
  
  public byte direction;
  
  public byte length;
  
  public UzhBody$Segment next;
  
  public UzhBody$Segment(UzhBody paramUzhBody, Point paramPoint, byte paramByte1, byte paramByte2) {
    this.head = paramPoint;
    this.direction = paramByte1;
    this.length = paramByte2;
  }
  
  public UzhBody$Segment(UzhBody paramUzhBody, Point paramPoint, byte paramByte) {
    this(paramUzhBody, paramPoint, paramByte, (byte)1);
  }
  
  public Point getTail() {
    Point point;
    (point = new Point(this.head)).a((byte)-this.direction, this.length);
    return point;
  }
  
  public boolean intersects(Point paramPoint) {
    switch (this.direction) {
      case -1:
        return (paramPoint.y == this.head.y && paramPoint.x >= this.head.x && paramPoint.x <= this.head.x + this.length);
      case 1:
        return (paramPoint.y == this.head.y && paramPoint.x <= this.head.x && paramPoint.x >= this.head.x - this.length);
      case 2:
        return (paramPoint.x == this.head.x && paramPoint.y >= this.head.y && paramPoint.y <= this.head.y + this.length);
      case -2:
        return (paramPoint.x == this.head.x && paramPoint.y <= this.head.y && paramPoint.y >= this.head.y - this.length);
    } 
    throw new RuntimeException("Invalid direction");
  }
  
  public String toString() {
    return "{head=" + this.head.toString() + "; direction=" + Point.directionToString(this.direction) + "; length=" + String.valueOf(this.length) + "}";
  }
}


/* Location:              /home/ubuntusfs/Downloads/Uzh.jar!/org/ugra/uzh/UzhBody$Segment.class
 * Java compiler version: 3 (47.0)
 * JD-Core Version:       1.1.3
 */