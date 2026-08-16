import java.util.*;

public class Solution {


    public static void main(String[] args) {

        class Pair {
            int start;
            int end;

            public Pair(int start, int end) {
                this.start = start;
                this.end = end;
            }
        }

        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int[] array = new int[n];
        for (int i=0; i<n; i++) array[i] = sc.nextInt();


        int maxLen = 0;
        int key = -1;
        HashMap<Integer, List<Pair>> ans = new HashMap<>();
        for (int i=0; i<n; i++){
            int currSum = 0;
            for (int j=i; j>=0; j--){
                currSum = currSum + array[j];
                if (!ans.containsKey(currSum)){
                    ans.put(currSum, new ArrayList<>());
                }
                List<Pair> pairs = ans.get(currSum);
                if (pairs.size() == 0 || pairs.get(pairs.size()-1).end <= j){
                    pairs.add(new Pair(j+1, i+1));
                }
                if (pairs.size() > maxLen){
                    maxLen = pairs.size();
                    key = currSum;
                }
            }

        }

        System.out.println(maxLen);
        for (Pair pair : ans.get(key)){
            System.out.println(pair.start + " " + pair.end);
        }

    }

}

