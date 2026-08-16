import java.util.ArrayList;
import java.util.Collections;
import java.util.HashMap;
import java.util.Scanner;

public final class DrazilAndFactorial {
    public static void main(String[] args) {
        Scanner sc=new Scanner(System.in);
        HashMap<Integer, ArrayList<Integer>> map=new HashMap<>();
        ArrayList<Integer> list=new ArrayList<>();
        list.add(3);
        list.add(2);
        list.add(2);
        map.put(4,list);
        ArrayList<Integer> list1=new ArrayList<>();
        list1.add(3);
        list1.add(5);
        map.put(6,list1);
        ArrayList<Integer> list2=new ArrayList<>();
        list2.add(2);
        list2.add(2);
        list2.add(2);
        list2.add(7);
        map.put(8,list2);
        ArrayList<Integer> list3=new ArrayList<>();
        list3.add(2);
        list3.add(3);
        list3.add(3);
        list3.add(7);
        map.put(9,list3);

        int n=sc.nextInt();
        String s=sc.next();
        ArrayList<Integer> ans=new ArrayList<>();
        for(int i=0;i<n;i++){
            int ind=s.charAt(i)-48;
            if(ind>1){
                if(!map.containsKey(ind)){
                    ans.add(ind);
                }else{
                    ans.addAll(map.get(ind));
                }
            }
        }
        Collections.sort(ans,Collections.reverseOrder());
        for(int ele:ans)
            System.out.print(ele);
        System.out.println();

    }
}
