import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
      	
        // 入力
        String s = sc.next();
      	int l=s.length();
      	
      if(s.charAt(l-1)=='s'){
      	System.out.println(s+"es");
      }else{
        System.out.println(s+"s");
      }
      

    }
}


