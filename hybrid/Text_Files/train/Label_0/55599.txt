import java.util.*;
public class Main{
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        Deque<String> deque = new ArrayDeque<>();
        while(sc.hasNext()){
            String data = sc.next();
            if(data.matches(".*[0-9].*"))
                deque.push(data);
            else{
                int num1 = Integer.parseInt(deque.pop());
                int num2 = Integer.parseInt(deque.pop());
                switch(data.charAt(0)){
                    case '+' : deque.push(String.valueOf(num2 + num1)); break;
                    case '-' : deque.push(String.valueOf(num2 - num1)); break;
                    case '*' : deque.push(String.valueOf(num2 * num1)); break;
                }
            }
        }
        System.out.println(Integer.parseInt(deque.pop()));
    }
}
