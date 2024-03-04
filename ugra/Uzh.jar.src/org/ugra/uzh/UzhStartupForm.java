package org.ugra.uzh;

import javax.microedition.lcdui.Command;
import javax.microedition.lcdui.CommandListener;
import javax.microedition.lcdui.Displayable;
import javax.microedition.lcdui.Form;
import javax.microedition.lcdui.Item;
import javax.microedition.lcdui.TextField;

public class UzhStartupForm extends Form implements CommandListener {
  private UzhMIDlet a;
  
  private Command a;
  
  private TextField a;
  
  public UzhStartupForm(UzhMIDlet paramUzhMIDlet) {
    super("Uzh");
    this.a = (TextField)paramUzhMIDlet;
    this.a = (TextField)new Command("Start", 4, 1);
    addCommand((Command)this.a);
    this.a = new TextField("Secret code", "", 6, 2);
    append((Item)this.a);
    setCommandListener(this);
  }
  
  public void commandAction(Command paramCommand, Displayable paramDisplayable) {
    if (paramCommand == this.a) {
      String str;
      if ((str = this.a.getString()).length() != 6)
        return; 
      this.a.startGame(Long.parseLong(str));
    } 
  }
}


/* Location:              /home/ubuntusfs/Downloads/Uzh.jar!/org/ugra/uzh/UzhStartupForm.class
 * Java compiler version: 3 (47.0)
 * JD-Core Version:       1.1.3
 */