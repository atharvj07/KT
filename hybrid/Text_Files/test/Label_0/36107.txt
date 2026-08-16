import java.util.*;
class Main {
    public static void main(String[] args) {
	Scanner sc = new Scanner(System.in);
	String str = sc.next();
	str = str.replace("1","*").replace("9","1").replace("*","9");
	System.out.println(str);
    }
}