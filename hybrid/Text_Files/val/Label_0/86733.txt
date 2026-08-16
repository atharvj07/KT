import java.util.*;

class Main {
    public static void main(String[] args) {
        String[] week = {"SUN","MON","TUE","WED","THU","FRI","SAT"};
        Scanner sc = new Scanner(System.in);
        String S = sc.next();

        for(int i=0; i<7; i++){
            if(S.equals(week[i])){
                System.out.println(7-i);
            }
        }
    }
}