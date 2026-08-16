import java.util.*;
public class MeetingFriends {
    public static void main(String args[]){
        Scanner scannerin=new Scanner(System.in);
        int firstperson_position=scannerin.nextInt();
        int secondperson_position=scannerin.nextInt();
        int thirderson_position=scannerin.nextInt();
        int[] arr_position={firstperson_position,secondperson_position,thirderson_position};
        Arrays.sort(arr_position);
        int answer=arr_position[2]-arr_position[0];
        System.out.println(answer);
    }
}
