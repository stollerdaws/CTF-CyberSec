package org.ugra.uzh;

import java.io.ByteArrayOutputStream;
import java.io.IOException;
import java.io.InputStream;
import java.io.OutputStream;
import javax.microedition.io.Connector;
import javax.microedition.io.HttpConnection;
import javax.microedition.lcdui.Canvas;
import javax.microedition.lcdui.Font;
import javax.microedition.lcdui.Graphics;
import javax.microedition.lcdui.Image;

public class UzhCanvas extends Canvas implements Runnable {
  private long a;
  
  private Thread a;
  
  private UzhWorld a;
  
  private ByteArrayOutputStream a;
  
  private byte a;
  
  private int a;
  
  private int b;
  
  private String a;
  
  private Font a;
  
  private Image a;
  
  private Graphics a = true;
  
  private int c;
  
  private int d;
  
  private int e;
  
  private int f;
  
  private int g;
  
  public UzhCanvas(long paramLong) {
    this.a = -1;
    this.b = 0;
    this.a = (Graphics)"";
    this.a = paramLong;
    int i = getWidth();
    int j = getHeight();
    this.a = (Graphics)Font.getDefaultFont();
    if (!isDoubleBuffered()) {
      this.a = (Graphics)Image.createImage(i, j);
      this.a = this.a.getGraphics();
      this.a.setFont((Font)this.a);
    } 
    int k = this.a.stringWidth("999");
    int m = (i - 2 - 2 - k) / 40;
    int n = (j - 2) / 30;
    this.c = Math.min(m, n);
    m = (i - this.c * 40 - 2) / 2;
    i = i - this.c * 40 - 2 - 2 - k;
    this.d = Math.min(m, i);
    this.e = (j - this.c * 30 - 2) / 2;
    this.f = 40 * this.c;
    this.g = 30 * this.c;
  }
  
  public void paint(Graphics paramGraphics) {
    if (this.a != null) {
      a(this.a);
      paramGraphics.drawImage((Image)this.a, 0, 0, 20);
      return;
    } 
    paramGraphics.setFont((Font)this.a);
    a(paramGraphics);
  }
  
  private void a(Graphics paramGraphics) {
    paramGraphics.setColor(255, 255, 255);
    paramGraphics.fillRect(0, 0, getWidth(), getHeight());
    if (this.a != null) {
      paramGraphics = paramGraphics;
      int i = (this = this).getWidth();
      paramGraphics.setColor(0, 0, 0);
      paramGraphics.fillRect(this.d, this.e, 2 + this.f, 1);
      paramGraphics.fillRect(this.d, this.e, 1, 2 + this.g);
      paramGraphics.fillRect(this.d + 1 + this.f, this.e, 1, 2 + this.g);
      paramGraphics.fillRect(this.d, this.e + 1 + this.g, 2 + this.f, 1);
      paramGraphics.setColor(0, 255, 0);
      UzhBody$Segment uzhBody$Segment = this.a.getBody().getTailSegment();
      while (true) {
        switch (uzhBody$Segment.direction) {
          case -1:
            a(paramGraphics, uzhBody$Segment.head.x, uzhBody$Segment.head.y, uzhBody$Segment.length, (byte)1);
            break;
          case 1:
            a(paramGraphics, (byte)(uzhBody$Segment.head.x - uzhBody$Segment.length + 1), uzhBody$Segment.head.y, uzhBody$Segment.length, (byte)1);
            break;
          case 2:
            a(paramGraphics, uzhBody$Segment.head.x, uzhBody$Segment.head.y, (byte)1, uzhBody$Segment.length);
            break;
          case -2:
            a(paramGraphics, uzhBody$Segment.head.x, (byte)(uzhBody$Segment.head.y - uzhBody$Segment.length + 1), (byte)1, uzhBody$Segment.length);
            break;
          default:
            throw new RuntimeException("Invalid direction");
        } 
        if ((uzhBody$Segment = uzhBody$Segment.next) == null) {
          paramGraphics.setColor(244, 193, 0);
          Point point = this.a.getFruit();
          a(paramGraphics, point.x, point.y, (byte)1, (byte)1);
          paramGraphics.setColor(0, 0, 0);
          paramGraphics.drawString(String.valueOf(this.a.getEatenFruits()), i - 1, this.e, 24);
          return;
        } 
      } 
    } 
    b(paramGraphics);
  }
  
  private void a(Graphics paramGraphics, byte paramByte1, byte paramByte2, byte paramByte3, byte paramByte4) {
    paramGraphics.fillRect(this.d + 1 + paramByte1 * this.c, this.e + 1 + (30 - paramByte4 - paramByte2) * this.c, paramByte3 * this.c, paramByte4 * this.c);
  }
  
  private void b(Graphics paramGraphics) {
    int i = getWidth();
    int j = getHeight();
    int k = this.a.getHeight();
    paramGraphics.setColor(0, 0, 0);
    i /= 2;
    j /= 3;
    paramGraphics.drawString("High score:", i, j, 17);
    j += k;
    paramGraphics.drawString(String.valueOf(this.b), i, j, 17);
    j += k + k / 2;
    if (this.a >= null) {
      paramGraphics.drawString("Last score:", i, j, 17);
      j += k;
      paramGraphics.drawString(String.valueOf(this.a), i, j, 17);
    } else {
      j += k;
    } 
    j += k + k / 2;
    if (!(this = (this.a != null) ? (UzhCanvas)this.a : (UzhCanvas)"Fetching results...").equals("")) {
      int m = 0;
      int n;
      for (n = indexOf('\n'); n != -1; n = indexOf('\n', m)) {
        paramGraphics.drawString(substring(m, n), i, j, 17);
        j += k;
        m = n + 1;
      } 
      paramGraphics.drawString(substring(m), i, j, 17);
    } 
  }
  
  protected void keyPressed(int paramInt) {
    switch (paramInt) {
      case -1:
      case 1:
      case 50:
        this.a = -2;
        break;
      case -2:
      case 6:
      case 56:
        this.a = 2;
        break;
      case -3:
      case 2:
      case 52:
        this.a = -1;
        break;
      case -4:
      case 5:
      case 54:
        this.a = true;
        break;
    } 
    if (this.a == null && (this = this).a == null) {
      this.a = (Graphics)new UzhWorld(this.a, this.a);
      this.a = (Graphics)new ByteArrayOutputStream();
      this.a.write(this.a);
      this.a = null;
      this.a = (Graphics)new Thread(this);
      this.a.start();
    } 
  }
  
  public void run() {
    try {
      repaint();
      while (true) {
        try {
          Thread.sleep(this.a.getStepDelay());
        } catch (InterruptedException interruptedException) {
          System.err.println(interruptedException);
        } 
        if (isShown()) {
          byte b;
          Graphics graphics = this.a;
          byte b1 = (this.a.getBody().getHeadSegment()).direction;
          if (graphics == Point.invertDirection(b1))
            b = b1; 
          this.a.write(b);
          if (!this.a.advance(b) || this.a.getEatenFruits() >= 10) {
            this.a = this.a.getEatenFruits();
            this.b = Math.max(this.b, this.a);
            return;
          } 
          repaint();
        } 
      } 
    } finally {
      a();
    } 
  }
  
  private void a() {
    this.a = null;
    this.a = (Graphics)"Fetching...";
    repaint();
    try {
      String str;
      HttpConnection httpConnection = (HttpConnection)Connector.open(str = "http://q.2024.ugractf.ru:9276/scores/?secret=" + this.a);
      try {
        httpConnection.setRequestMethod("POST");
        httpConnection.setRequestProperty("Content-Type", "application/octet-stream");
        OutputStream outputStream;
        (outputStream = httpConnection.openOutputStream()).write(this.a.toByteArray());
        outputStream.close();
        int i;
        if ((i = httpConnection.getResponseCode()) != 200) {
          this.a = (Graphics)("Error " + i + ": " + httpConnection.getResponseMessage());
        } else {
          InputStream inputStream = httpConnection.openInputStream();
          ByteArrayOutputStream byteArrayOutputStream = new ByteArrayOutputStream();
          byte[] arrayOfByte = new byte[128];
          int j;
          while ((j = inputStream.read(arrayOfByte)) != -1)
            byteArrayOutputStream.write(arrayOfByte, 0, j); 
          inputStream.close();
          this.a = (Graphics)byteArrayOutputStream.toString();
        } 
      } finally {
        httpConnection.close();
      } 
    } catch (IOException iOException) {
      this.a = (Graphics)iOException.toString();
    } 
    repaint();
    this.a = null;
  }
}


/* Location:              /home/ubuntusfs/Downloads/Uzh.jar!/org/ugra/uzh/UzhCanvas.class
 * Java compiler version: 3 (47.0)
 * JD-Core Version:       1.1.3
 */