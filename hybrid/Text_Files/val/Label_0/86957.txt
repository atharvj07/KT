import java.util.*;

public class Main{
	
  public static void main(String[] args){
    Scanner sc = new Scanner(System.in);
  	char[] ch=sc.next().toCharArray();
    int f=0;
    for(int i=0;i<6;i++){
      if(ch[i]=='1'){
        f++;
      }
    }
    System.out.println(f);
    
  }
}
