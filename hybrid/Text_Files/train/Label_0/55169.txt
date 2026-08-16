import java.util.Scanner;

public class UltraFastMathematician {

    
    public static void main(String[] args) {
    Scanner sc=new Scanner(System.in);
    String s1=sc.next();
    String s2=sc.next();
    String s="";
    for (int i = 0; i < s1.length(); i++) {
        char c1=s1.charAt(i);
        char c2=s2.charAt(i);
        if((c1=='0' && c2=='1') ||(c2=='0' && c1=='1'))
            s+="1";
        else
            s+="0";
    }
    System.out.println(s);
    
    }

}
