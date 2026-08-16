import java.util.*;
import java.util.function.BiFunction;
import java.util.function.*;
import java.util.stream.Collectors;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String s = sc.nextLine();
        long j = 0 ;
        List<Character> ls = new LinkedList<>();
        for(char c: s.toCharArray())
            ls.add(c);

        System.out.println(ls.stream().distinct().map(e -> solve.apply(e,s)).min(Comparator.naturalOrder()).get());


    }



    static BiFunction<String,Character,String> step = (before,c) -> {
        String s1,s2;
        StringBuilder sb = new StringBuilder();
        if(before !=  null && before.length() > 0) {
            s1 = before.substring(0, before.length() - 1);
            s2 = before.substring(1,before.length());
            for(int i = 0;i < before.length() -1;i++)
            {
                if(c.equals(s1.charAt(i)) || c.equals(s2.charAt(i)))
                {
                    sb.append(c);
                }
                else
                    sb.append(s1.charAt(i));
            }
            return sb.toString();
        }
        else
            return "";
    };

    static Predicate<String> check = s -> {
        List<Character> ls = new LinkedList<>();
        for(char c: s.toCharArray())
            ls.add(c);
        if(ls.stream().distinct().count() == 1)
            return true;
        else
            return false;
    };
    static BiFunction<Character,String,Integer> solve = (c,s) -> {
        for (int i = 0; ; i++) {
            if (check.test(s))
                return i;
            else
                s = step.apply(s,c);
        }
    };
}
