
import java.util.Scanner;

public class Main {
  public static void main(String[] args){
    Scanner sc = new Scanner(System.in);
    String s = sc.next();
    char[] out = s.toCharArray();
    
    int index = 0;
    if(out[index] == '?') out[index] = 'D';
    index++;
    while(index < out.length) {
      if(out[index] == '?') {
        if(out[index-1] == 'P') {
          out[index] = 'D';
        }
        else {
          if(index < out.length - 1 && out[index+1] == '?') {
            out[index] = 'P';
            out[index+1] = 'D';
          }
          else {
            out[index] = 'D';
          }
        }
      }
      index++;
    }
    
    
    String outStr = new String(out);
    System.out.println(outStr);
    
  }
}
