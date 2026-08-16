/*
 * To change this template, choose Tools | Templates
 * and open the template in the editor.
 */

/**
 *
 * @author YaSeR
 */
import java.io.File;
import java.io.IOException;
import java.util.Scanner;

public class WayTooLongWords {
    public static void main(String[] args) throws IOException{
        //Scanner cs = new Scanner(new File("C:\\Users\\YaSeR\\Documents\\NetBeansProjects\\ACM\\src\\WayTooLongWords.txt"));
        Scanner cs = new Scanner(System.in);
        int no = cs.nextInt();
        String [] array = new String[no];
        String firstchar = "";
        String lastchar = "";
        int midchar = 0;

        for(int i=0 ; i<no ; i++)
        {
            array[i] = cs.next();
        }

        for(int j =0 ; j<array.length;j++)
        {
            if(array[j].length() <= 10)
            {
                System.out.println(array[j]);
            }
            else
            {
                firstchar = String.valueOf(array[j].charAt(0));
                lastchar = String.valueOf(array[j].charAt(array[j].length()-1));
                for(int h=1 ;h<=array[j].length()-2;h++ )
                {
                    midchar ++;
                }
                System.out.println(firstchar+""+midchar+""+lastchar);
                midchar = 0;
            }
            
        }
        
        
    }
}
