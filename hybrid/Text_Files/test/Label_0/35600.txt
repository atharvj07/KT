    import java.util.ArrayList;
    import java.util.List;
    import java.util.Collections;
    import java.util.Scanner;
public class Main {
    public static void main(String[] args) {
        List<Integer> chao = new ArrayList<>();
        Scanner sc = new Scanner(System.in);
        int i,b,f,x=0;
        String a;
        char c;
        a = sc.next();
        b = a.length();
        for(i=0;i<b;i++){
            c = a.charAt(i);
            if(c!='+'){
                chao.add((int)c);
                x++;
            }    
        }
        Collections.sort(chao);
        for(i=0;i<x;i++){
            f=chao.get(i);
            System.out.print((char)f);
            if(i!=(x-1)){
                System.out.print("+");
            }
        }
    }
}
	 	 		   						  	 		   							