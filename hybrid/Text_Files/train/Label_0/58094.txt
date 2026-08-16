import java.util.Scanner;

class Main{
  public static void main(String[] args){
    Scanner scan = new Scanner(System.in);
    char[] s = scan.next().toCharArray();
    char[] t = scan.next().toCharArray();
    scan.close();
    
    for(int i=0;i<s.length;i++){
      if(s[i]==t[i]){continue;}
      else{
        char c1=s[i];
        char c2=t[i];
        for(int j=0;j<i;j++){
          if(s[j]==c1||s[j]==c2){
            System.out.println("No");
            return;
          }
        }
        for(int j=i;j<s.length;j++){
          if(s[j]==c1){
            s[j]=c2;
          }else if(s[j]==c2){
            s[j]=c1;
          }
        }
      }
    }
    
    System.out.println("Yes");
    return;
  }
}