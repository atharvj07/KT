import java.util.*;

class Main{
    public static void main(String args[]){
        Scanner sc=new Scanner(System.in);
        while(sc.hasNext()){
            System.out.printf("3C%02d\n",(sc.nextInt()-1)%39+1);
        }
    }
}
