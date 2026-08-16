import java.util.Scanner;

class Main{
    
    private static int a,b;
public static void main(String[] args){
    
    Scanner s= new Scanner(System.in);
a=s.nextInt();
b=s.nextInt();
System.out.printf("%d %d %.5f\n", (a/b),(a%b),((double)a/b));
    
}
}

