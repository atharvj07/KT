
import org.omg.CORBA.INTERNAL;
import sun.awt.image.ImageWatched;
import sun.reflect.generics.tree.Tree;

import java.nio.channels.ScatteringByteChannel;
import java.text.SimpleDateFormat;
import java.util.*;

public final class Main {

    public static void main(String[] args) {

        Scanner s = new Scanner(System.in);


        int TC = s.nextInt();


        for (int tc = 0; tc < TC; tc++) {

            boolean[] array = new boolean[26];

            String str = s.next();


            for (int i = 0; i < str.length(); i++) {

                if (i == str.length()-1) array[str.charAt(i)-'a'] = true;
                else {

                    char now = str.charAt(i);

                    char next = str.charAt(i+1);

                    if (next == now) i+=1 ;

                    else array[now - 'a'] = true;
                }

            }

            for (int i = 0 ; i < array.length; i++) {

                if (array[i]) {

                    char print = (char) (i + 'a');
                    System.out.print(print);
                }
            }

            System.out.print("\n");

        }
    }

}