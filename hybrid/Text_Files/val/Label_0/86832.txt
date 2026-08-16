import java.util.*;

public class Main{
    public static int helper(int i, List<Integer> list) {
        for (int j = 0; j < list.size(); j++) {
            int cur = list.get(j);
            if (cur > i)
                return j;
        }
        return list.size();
    }

    public static void main(String[] args) {
        /* 00000001
        Scanner x = new Scanner(System.in);
        int n = x.nextInt();
        int[] a = new int[n];
        for (int i = 0; i < n; i++)
            a[i] = x.nextInt();
        int ans = -1;

        if (a[0] != 0)
            ans = 1;
        else {
            int max = 0;
            for (int i = 1; i < n; i++) {
                if (a[i] < 0 || a[i] > max + 1) {
                    ans = i + 1;
                    break;
                }
                max = Math.max(max, a[i]);
            }
        }
        System.out.println(ans);
        */
        Scanner x = new Scanner(System.in);
        int n = x.nextInt();
        int[] l = new int[n];
        int[] r = new int[n];
        for (int i = 0; i < n; i++)
            l[i] = x.nextInt();
        for (int i = 0; i < n; i++)
            r[i] = x.nextInt();

        List<List<Integer>> list = new ArrayList<List<Integer>>();
        List<Integer> zeroList = new ArrayList<>();
        List<Integer> zeroListNew = new ArrayList<>();
        Set<Integer> visited = new HashSet<>();
        Map<Integer, List<Integer>> map = new HashMap<Integer, List<Integer>>();

        for (int i = 0; i < n; i++) {
            List<Integer> pair = new ArrayList<>();
            pair.add(l[i]);
            pair.add(r[i]);
            list.add(pair);
            if (l[i] == 0 && r[i] == 0) {
                zeroList.add(i);
            }
        }

        if (zeroList.size() == 0) {
            System.out.println("NO");
            return;
        }

        int id = 1;
        while (visited.size() < n && zeroList.size() > 0) {
            for (int i = 0; i < n; i++) {
                if (zeroList.indexOf(i) >= 0 || visited.contains(i))
                    continue;
                int leftZero = helper(i, zeroList);
                int rightZero = zeroList.size() - leftZero;
                int lNew = list.get(i).get(0) - leftZero;
                int rNew = list.get(i).get(1) - rightZero;

                if (lNew < 0 || rNew < 0) {
                    System.out.println("NO");
                    return;
                }
                list.get(i).set(0, lNew);
                list.get(i).set(1, rNew);

                if (lNew == 0 && rNew == 0) {
                    zeroListNew.add(i);
                }
            }

            for (Integer j : zeroList)
                visited.add(j);
            map.put(id, new ArrayList<Integer>(zeroList));
            id += zeroList.size();
            zeroList.clear();
            zeroList.addAll(zeroListNew);
            zeroListNew.clear();
        }
        if (visited.size() < n) {
            System.out.println("NO");
            return;
        }
        int[] res = new int[n];
        System.out.println("YES");
        for (Integer i : map.keySet())
            for (Integer j : map.get(i))
                res[j] = n - i + 1;

        for (int i = 0; i < n; i++) {
            System.out.print(res[i]);
            System.out.print(" ");
        }
        System.out.println("");
    }













    }
