package Tasks;

import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.chrome.ChromeDriver;
import org.openqa.selenium.interactions.Actions;
import org.openqa.selenium.support.ui.ExpectedConditions;
import org.openqa.selenium.support.ui.WebDriverWait;

import java.time.Duration;
import java.time.Instant;
import java.util.Set;
import java.util.concurrent.TimeUnit;

public class Task4 {
    public static void main(String[] args) throws InterruptedException {
        System.setProperty("webdriver.chrome.driver", "C:\\Users\\odunuga\\kehinde-testify\\SeleniumWeb\\src\\chromedriver.exe");
        //Launch browser
        WebDriver driver = new ChromeDriver();
        //Maximize the browser
        driver.manage().window().maximize();
        // Manage wait time
        driver.manage().timeouts().implicitlyWait(5, TimeUnit.SECONDS);

        //Navigate to the url
        driver.get("http://demo.guru99.com/");
        Thread.sleep(2000);

        driver.findElement(By.linkText("Security Project")).click();
        Thread.sleep(3000);
        
        Set<String> windows = driver.getWindowHandles();
        for (String window: windows) {
            driver.switchTo().window(window);
            Thread.sleep(3000);
            System.out.println(driver.getCurrentUrl());

            WebElement compAccess = driver.findElement(By.xpath("//*[@id=\"ad_position_box\"]"));
            Actions mouse = new Actions(driver);
            mouse.moveToElement(compAccess).build().perform();
            Thread.sleep(1000);

            if (driver.getCurrentUrl().equalsIgnoreCase("https://demo.guru99.com/#google_vignette")) {
                //apple = driver.getCurrentUrl();
                driver.findElement(By.xpath("/html/body")).click();
                Thread.sleep(3000);
            }
        }
        //input a text in the username and password
        driver.findElement(By.xpath("//tbody/tr[1]/td[2]/input[1]")).sendKeys("testify");
        driver.findElement(By.xpath("//tbody/tr[2]/td[2]/input[1]")).sendKeys("school");

        Thread.sleep(3000);

        driver.quit();
    }
}
