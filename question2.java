import java.util.Scanner;

import javax.sound.midi.MidiChannel;

public class question2{
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        System.out.println("Welcome To KM to meter inches feet inches and centimeter terminal");
        System.out.println("\nEnter distance in KM: ");
        double dist = input.nextDouble();
        System.out.println("Distance in feet: "+  dist* 3280.8 +"ft");
        System.out.println("Distance in meter: "+ dist* 1000+"m");
        System.out.println("Distance in centimeter: "+ dist*100000+"cm");
        System.out.println("Distance in inches: "+ dist*39370+"in");

    }
}