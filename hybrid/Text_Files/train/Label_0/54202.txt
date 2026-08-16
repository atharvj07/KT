import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        Integer n = sc.nextInt();
        Deque <Integer> deque = new ArrayDeque<Integer>();
        for(int i = 0; i < n; i++){
            String command = sc.next();
            if(command.equals("insert")){
                Integer number = Integer.parseInt(sc.next());
                deque.push(number);
            }else if(command.equals("delete")){
                Integer number = Integer.parseInt(sc.next());
                deque.remove(number);
            }else if(command.equals("deleteFirst")){
                deque.removeFirst();
            }else{
                deque.removeLast();
            }
        }
        StringBuilder sb = new StringBuilder();
        sb.append(deque.poll());
        for(int num : deque)
            sb.append(" ").append(num);
        
        System.out.println(sb);

    }
}
