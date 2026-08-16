import java.io.*;
public class Main {
 public static void main(String[] args){
  try{
  BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
   char botton[][]={{' '},
                            {'\'' , ',' , '.' , '!' , '?'},
                            {'a' , 'b' , 'c' , 'A' , 'B' , 'C'},
                            {'d' , 'e' , 'f' , 'D' , 'E' , 'F'},
                            {'g' , 'h' , 'i' , 'G' , 'H' , 'I'},
                            {'j' , 'k' , 'l' , 'J' , 'K' , 'L'},
                            {'m' , 'n' , 'o' , 'M' , 'N' , 'O'},
                            {'p' , 'q' , 'r', 's' , 'P' , 'Q' , 'R' , 'S'},
                            {'t' , 'u' , 'v' , 'T' , 'U' , 'V'},
                            {'w' , 'x' , 'y' , 'z' , 'W' , 'X' , 'Y' , 'Z'}};
    int n[]={0,5,6,6,6,6,6,8,6,8};
    while(true){
     String s=br.readLine();
     s+="x";
     int sl=s.length();
     int cnt=1;
     
     for(int i=1;i<sl;i++){
      char x,ch;
      if(s.charAt(i-1)!=s.charAt(i)){
      x=s.charAt(i-1);
      if(x!='0'){
       ch=botton[x-'0'][(cnt-1)%n[x-'0']];
       System.out.print(ch);
      }
      else if(x=='0')for(int j=0;j<cnt-1;j++)System.out.print(" ");
      cnt=0;
      cnt++;
     }
     else cnt++;
    }
    System.out.print("\n");
  }
 }
 catch(Exception e){return ;}
}
}
