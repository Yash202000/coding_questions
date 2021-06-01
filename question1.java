/*

Ramesh's basic salary is input through the keyboard. His dearness allowance is 40% of basic salary,
and house rent allowance is 20% of basic salary. Write a program to calculate his gross salary.

*/

import java.util.Scanner;

public class question1{
    public static void main(String[] args) {
        System.out.println("Welcome To Gross salary formula terminal");
        //defined scanner input
        Scanner input = new Scanner(System.in);
        System.out.println("\nEnter your salary: ");
        float salary = input.nextFloat();
        
        //calculatin dearness and houseRent
        float dearness =  (float)0.4*salary;
        float houseRent = (float)0.2*salary;

        Float grossSalary = dearness+houseRent+salary;
        System.out.println("dearness: "+ dearness);
        System.out.println("houseRent: "+ houseRent);
        System.out.println("Gross Salary: "+ grossSalary);
        
    }
}