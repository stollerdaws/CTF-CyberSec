package org.ugra.uzh;

public class UzhBody {
  private UzhBody$Segment a;
  
  private UzhBody$Segment b;
  
  private byte a = 1;
  
  public UzhBody(Point paramPoint, byte paramByte) {
    this(paramPoint, paramByte, (byte)1);
  }
  
  public UzhBody(Point paramPoint, byte paramByte1, byte paramByte2) {
    this.a = this.b = new UzhBody$Segment(this, paramPoint, paramByte1, paramByte2);
  }
  
  public UzhBody$Segment getHeadSegment() {
    return this.a;
  }
  
  public UzhBody$Segment getTailSegment() {
    return this.b;
  }
  
  public byte getSegmentsCount() {
    return this.a;
  }
  
  public void advanceHead(byte paramByte) {
    if (paramByte == this.a.direction) {
      this.a.head.a(paramByte, (byte)1);
      this.a.length = (byte)(this.a.length + 1);
      return;
    } 
    Point point;
    (point = new Point(this.a.head)).a(paramByte, (byte)1);
    UzhBody$Segment uzhBody$Segment = new UzhBody$Segment(this, point, paramByte);
    this.a.next = uzhBody$Segment;
    this.a = uzhBody$Segment;
    this.a = (byte)(this.a + 1);
  }
  
  public void shrinkTail() {
    if (this.b.length == 1) {
      this.b = this.b.next;
      this.a = (byte)(this.a - 1);
      return;
    } 
    this.b.length = (byte)(this.b.length - 1);
  }
  
  public boolean headIntersects() {
    Point point = this.a.head;
    UzhBody$Segment uzhBody$Segment = this.b;
    for (byte b = 0; b < this.a - 3; b = (byte)(b + 1)) {
      if (uzhBody$Segment.intersects(point))
        return true; 
      uzhBody$Segment = uzhBody$Segment.next;
    } 
    return false;
  }
  
  public boolean pointIntersects(Point paramPoint) {
    UzhBody$Segment uzhBody$Segment = this.b;
    while (true) {
      if (intersects(paramPoint))
        return true; 
      if ((uzhBody$Segment = this.next) == null)
        return false; 
    } 
  }
}


/* Location:              /home/ubuntusfs/Downloads/Uzh.jar!/org/ugra/uzh/UzhBody.class
 * Java compiler version: 3 (47.0)
 * JD-Core Version:       1.1.3
 */