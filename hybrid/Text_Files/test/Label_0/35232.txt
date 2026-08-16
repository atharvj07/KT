import java.util.*;


public class Main {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        ArrayList<Integer> arrayList = new ArrayList<Integer>();
        int n = scanner.nextInt();
        int count=0;
        for(int i = 0; i<n;i++){
            int a = scanner.nextInt();
            if(!arrayList.contains(a)&&a!=0){
                arrayList.add(a);

            }
        }
        System.out.println(arrayList.size());



            }
        }

