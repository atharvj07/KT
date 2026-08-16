import java.util.Scanner;
import java.util.Collections;
import java.util.ArrayList;
import java.util.Comparator;
public class Main {
    static class pair{
        char c;
        int index;
        public pair(char c,int index){
            this.c = c;
            this.index = index;
        }
    }
    public static void main(String args[]) {
        Scanner s = new Scanner(System.in);
        int n = s.nextInt();
        String a = s.next();
        String b = s.next();
        ArrayList<pair> list1 = new ArrayList<>();
        ArrayList<pair> list2 = new ArrayList<>();
        ArrayList<Integer> question1 = new ArrayList<>();
        ArrayList<Integer> question2 = new ArrayList<>();
        for(int i = 0; i < n; i++){
            if(a.charAt(i) != '?'){
                list1.add(new pair(a.charAt(i),i + 1));
            }
            else{
                question1.add(i + 1);
            }
        
        }
        for(int i = 0; i < n; i++){
            if(b.charAt(i) != '?'){
                list2.add(new pair(b.charAt(i),i + 1));
            }
            else{
                question2.add(i + 1);
            }
        }
        Collections.sort(list1,new Comparator<pair>(){
            public int compare(pair a,pair b){
                if(a.c == b.c){
                    return a.index - b.index;
                }
                return a.c - b.c;
            }
        });
        Collections.sort(list2,new Comparator<pair>(){
            public int compare(pair a,pair b){
                if(a.c == b.c){
                    return a.index - b.index;
                }
                return a.c - b.c;
            }
        });
        ArrayList<ArrayList<Integer>> ans = new ArrayList<>();
      
        ArrayList<Integer> curr1 = new ArrayList<>();
        ArrayList<Integer> curr2 = new ArrayList<>();
        int i = 0,j = 0,k1 = 0,k2 = 0;
        while(i < list1.size() && j < list2.size()){
            if(list1.get(i).c == list2.get(j).c){
                ArrayList<Integer> curr = new ArrayList<>();
                curr.add(list1.get(i).index);
                curr.add(list2.get(j).index);
                ans.add(new ArrayList<>(curr));
                i++;
                j++;
            }
            else if(list1.get(i).c > list2.get(j).c){
                curr2.add(list2.get(j).index);
                j++;
            }
            else{
                curr1.add(list1.get(i).index);
                i++;
            }
        }
        while(i < list1.size()){
             curr1.add(list1.get(i).index);
             i++;
        }
        while(j < list2.size()){
            curr2.add(list2.get(j).index);
            j++;

        }
       
        i = 0;
        while(i < curr1.size() && k2 < question2.size()){
                ArrayList<Integer> curr = new ArrayList<>();
                curr.add(curr1.get(i));
                curr.add(question2.get(k2));
                ans.add(new ArrayList<>(curr));
                i++;
                k2++;

        }
        j = 0;
        while(j < curr2.size() && k1 < question1.size()){
                ArrayList<Integer> curr = new ArrayList<>();
                curr.add(question1.get(k1));
                curr.add(curr2.get(j));
                ans.add(new ArrayList<>(curr));
                j++;
                k1++;

        }
          while(k1 < question1.size() && k2 < question2.size()){
             ArrayList<Integer> curr = new ArrayList<>();
                curr.add(question1.get(k1));
                curr.add(question2.get(k2));
                ans.add(new ArrayList<>(curr));
                k1++;
                k2++;
        }
        System.out.println(ans.size());
        for(i = 0; i < ans.size(); i++){
            System.out.println(ans.get(i).get(0) + " " + ans.get(i).get(1));
        }
    }
}