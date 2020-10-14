package org.springframework.samples.petclinic.customers.model;
import static org.junit.jupiter.api.Assertions.assertEquals;
import java.util.Date;
import org.junit.jupiter.api.Test;
public class PetTest {
    @Test
    public void testGetName(){
        //Arrange
        Pet pet = new Pet();
        //Act
        pet.setName("Fluffy");
        //Assert
        assertEquals("Fluffy", pet.getName());
    }
    @Test
    public void testGetOwner(){
        //Arrange
        Pet pet = new Pet();
        Owner owner = new Owner();
<<<<<<< HEAD
        owner.setFirstName("Call");
=======
        owner.setFirstName("Call2");
>>>>>>> feature/msp-9
        //Act
        pet.setOwner(owner);
        //Assert
        assertEquals("Call", pet.getOwner().getFirstName());
    }
    @Test
    public void testBirthDate(){
        //Arrange
<<<<<<< HEAD
        Pet pet = new Pet()
=======
        Pet pet = new Pet();
>>>>>>> feature/msp-9
        Date bd = new Date();
        //Act
        pet.setBirthDate(bd);
        //Assert
        assertEquals(bd,pet.getBirthDate());
    }
<<<<<<< HEAD
    
=======
>>>>>>> feature/msp-9
}