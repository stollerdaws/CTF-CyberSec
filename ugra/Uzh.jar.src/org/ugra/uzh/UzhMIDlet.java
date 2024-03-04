package org.ugra.uzh;

import javax.microedition.lcdui.Display;
import javax.microedition.lcdui.Displayable;
import javax.microedition.midlet.MIDlet;

public class UzhMIDlet extends MIDlet {
  private Display a;
  
  public void startApp() {
    this.a = Display.getDisplay(this);
    UzhStartupForm uzhStartupForm = new UzhStartupForm(this);
    this.a.setCurrent((Displayable)uzhStartupForm);
  }
  
  public void pauseApp() {}
  
  public void destroyApp(boolean paramBoolean) {}
  
  public void startGame(long paramLong) {
    UzhCanvas uzhCanvas = new UzhCanvas(paramLong);
    this.a.setCurrent((Displayable)uzhCanvas);
  }
}


/* Location:              /home/ubuntusfs/Downloads/Uzh.jar!/org/ugra/uzh/UzhMIDlet.class
 * Java compiler version: 3 (47.0)
 * JD-Core Version:       1.1.3
 */