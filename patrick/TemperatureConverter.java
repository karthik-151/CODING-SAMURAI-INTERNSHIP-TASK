import java.util.Scanner;

public class TemperatureConverter {

    // Method to convert Celsius to Fahrenheit
    public static double celsiusToFahrenheit(double c) {
        return (c * 9 / 5) + 32;
    }

    // Method to convert Fahrenheit to Celsius
    public static double fahrenheitToCelsius(double f) {
        return (f - 32) * 5 / 9;
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.println("🌡️ Temperature Converter");
        System.out.println("1. Celsius ➝ Fahrenheit");
        System.out.println("2. Fahrenheit ➝ Celsius");

        System.out.print("Enter your choice (1/2): ");
        int choice = scanner.nextInt();

        if (choice == 1) {
            System.out.print("Enter temperature in Celsius: ");
            double celsius = scanner.nextDouble();
            double fahrenheit = celsiusToFahrenheit(celsius);
            System.out.printf("%.2f°C = %.2f°F\n", celsius, fahrenheit);

        } else if (choice == 2) {
            System.out.print("Enter temperature in Fahrenheit: ");
            double fahrenheit = scanner.nextDouble();
            double celsius = fahrenheitToCelsius(fahrenheit);
            System.out.printf("%.2f°F = %.2f°C\n", fahrenheit, celsius);

        } else {
            System.out.println("❌ Invalid choice! Please enter 1 or 2.");
        }

        scanner.close();
    }
}