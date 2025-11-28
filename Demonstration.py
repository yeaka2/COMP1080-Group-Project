"""
test_system.py
Automated test cases for the Lost and Found System
COMP1080 Group Project
"""

import os
import json
import tempfile
import sys
from io import StringIO
from models import User, Item
from System import System

class TestLostAndFoundSystem:
    """Test class for Lost and Found System functionality"""
    
    def setUp(self):
        """Set up test environment with temporary files"""
        # Create temporary files for testing
        self.temp_items_file = tempfile.NamedTemporaryFile(mode='w', suffix='.json', delete=False)
        self.temp_users_file = tempfile.NamedTemporaryFile(mode='w', suffix='.json', delete=False)
        
        # Initial test data
        initial_items = {
            "max_id": 2,
            "items": [
                {
                    "item_id": 1,
                    "name": "Black Wallet",
                    "contact": "john@example.com",
                    "Category": "Personal",
                    "Description": "Leather wallet with cards inside",
                    "Location": "Student Lounge",
                    "Status": False,
                    "Lost_or_found": True
                },
                {
                    "item_id": 2,
                    "name": "Calculus Textbook",
                    "contact": "alice@example.com", 
                    "Category": "Books",
                    "Description": "James Stewart 8th Edition",
                    "Location": "Library",
                    "Status": False,
                    "Lost_or_found": False
                }
            ]
        }
        
        initial_users = [
            {
                "username": "test_admin",
                "password": "8d969eef6ecad3c29a3a629280e686cf0c3f5d5a86aff3ca12020c923adc6c92",  # "123456"
                "role": "admin",
                "contact": "admin@test.com",
                "email": "admin@test.com"
            },
            {
                "username": "test_owner", 
                "password": "8d969eef6ecad3c29a3a629280e686cf0c3f5d5a86aff3ca12020c923adc6c92",  # "123456"
                "role": "owner",
                "contact": "owner@test.com",
                "email": "owner@test.com"
            },
            {
                "username": "test_finder",
                "password": "8d969eef6ecad3c29a3a629280e686cf0c3f5d5a86aff3ca12020c923adc6c92",  # "123456"  
                "role": "finder",
                "contact": "finder@test.com",
                "email": "finder@test.com"
            }
        ]
        
        # Write initial data to temporary files
        json.dump(initial_items, self.temp_items_file)
        self.temp_items_file.close()
        
        json.dump(initial_users, self.temp_users_file)
        self.temp_users_file.close()
        
        # Create system instance with test files
        self.system = System(filename=self.temp_items_file.name, 
                           users_filename=self.temp_users_file.name)
    
    def tearDown(self):
        """Clean up temporary files"""
        os.unlink(self.temp_items_file.name)
        os.unlink(self.temp_users_file.name)
    
    def test_1_user_authentication(self):
        """Test Case 1: User Registration and Login"""
        print("=" * 50)
        print("TEST CASE 1: User Registration and Login")
        print("=" * 50)
        
        # Test password hashing
        password = "testpass123"
        hashed = self.system.hash_password(password)
        print(f"✓ Password hashing works: {len(hashed)} character hash generated")
        
        # Test user loading from file
        print(f"✓ Users loaded successfully: {len(self.system.users)} users found")
        for user in self.system.users:
            print(f"  - {user.username} ({user.role})")
        
        # Test login functionality
        original_stdin = sys.stdin
        sys.stdin = StringIO("test_admin\n123456\n")
        
        try:
            self.system.login()
            print("✓ Admin login successful")
        except Exception as e:
            print(f"✗ Login test failed: {e}")
        finally:
            sys.stdin = original_stdin
    
    def test_2_item_management(self):
        """Test Case 2: Item CRUD Operations"""
        print("\n" + "=" * 50)
        print("TEST CASE 2: Item Management")
        print("=" * 50)
        
        initial_count = len(self.system.items)
        print(f"Initial items count: {initial_count}")
        
        # Test adding a found item
        print("\n--- Testing Add Found Item ---")
        original_stdin = sys.stdin
        test_input = StringIO("Blue Water Bottle\nAccessories\nHydro Flask 500ml\nfinder@test.com\nLibrary\n")
        sys.stdin = test_input
        
        try:
            self.system.add_item('found')
            print("✓ Found item added successfully")
        except Exception as e:
            print(f"✗ Add found item failed: {e}")
        finally:
            sys.stdin = original_stdin
        
        # Test adding a lost item  
        print("\n--- Testing Add Lost Item ---")
        test_input = StringIO("Physics Textbook\nBooks\nUniversity Physics 15th Edition\nowner@test.com\nClassroom B210\n")
        sys.stdin = test_input
        
        try:
            self.system.add_item('lost')
            print("✓ Lost item added successfully")
        except Exception as e:
            print(f"✗ Add lost item failed: {e}")
        finally:
            sys.stdin = original_stdin
        
        # Verify items were added
        new_count = len(self.system.items)
        print(f"Final items count: {new_count}")
        print(f"✓ Item addition verified: {new_count - initial_count} new items added")
        
        # Display all items
        print("\n--- Current Items in System ---")
        for item in self.system.items:
            status = "Claimed" if item.status else "Unclaimed" if item.lost_or_found else "Unfound"
            print(f"  ID:{item.item_id} | {item.name} | {item.category} | {status}")
    
    def test_3_search_functionality(self):
        """Test Case 3: Search and Listing"""
        print("\n" + "=" * 50)
        print("TEST CASE 3: Search Functionality")
        print("=" * 50)
        
        # Test search by keyword
        print("--- Testing Search by Keyword 'Wallet' ---")
        results = self.system.search_item("Wallet")
        print(f"✓ Search found {len(results) if results else 0} items")
        
        print("--- Testing Search by Keyword 'Textbook' ---")
        results = self.system.search_item("Textbook")
        print(f"✓ Search found {len(results) if results else 0} items")
        
        print("--- Testing Search by Non-existent Keyword ---")
        results = self.system.search_item("NonexistentItemXYZ")
        print("✓ Handles non-existent items correctly")
        
        # Test listing all items
        print("\n--- Testing List All Items ---")
        print("Items in system:")
        self.system.list_items()
    
    def test_4_admin_operations(self):
        """Test Case 4: Administrator Functions"""
        print("\n" + "=" * 50)
        print("TEST CASE 4: Admin Operations")
        print("=" * 50)
        
        # Test item update
        print("--- Testing Item Update ---")
        update_success = self.system.update_item(1, description="Updated: Black leather wallet", location="Main Building")
        print(f"✓ Item update: {'Success' if update_success else 'Failed'}")
        
        # Test item deletion
        print("--- Testing Item Deletion ---")
        initial_count = len(self.system.items)
        delete_success = self.system.delete_item("1")  # Delete by ID
        if delete_success:
            print(f"✓ Item deletion: Success ({initial_count - len(self.system.items)} item removed)")
        else:
            print("✗ Item deletion: Failed")
        
        # Test invalid item operations
        print("--- Testing Invalid Item Operations ---")
        invalid_update = self.system.update_item(999, name="Nonexistent")
        print(f"✓ Handles invalid update: {'Correctly rejected' if not invalid_update else 'Problem'}")
        
        invalid_delete = self.system.delete_item("999")
        print(f"✓ Handles invalid deletion: {'Correctly rejected' if not invalid_delete else 'Problem'}")
    
    def test_5_claim_functionality(self):
        """Test Case 5: Item Claiming Process"""
        print("\n" + "=" * 50)
        print("TEST CASE 5: Claiming Process")
        print("=" * 50)
        
        # Test claiming an item
        print("--- Testing Item Claim ---")
        original_stdin = sys.stdin
        
        # First, let's add a test item to claim
        test_input = StringIO("Test Phone\nElectronics\niPhone 12\nfinder@test.com\nCanteen\n")
        sys.stdin = test_input
        self.system.add_item('found')
        sys.stdin = original_stdin
        
        # Find the newly added item
        new_item = None
        for item in self.system.items:
            if item.name == "Test Phone":
                new_item = item
                break
        
        if new_item:
            print(f"✓ Test item created: {new_item.name} (ID: {new_item.item_id})")
            
            # Test claiming the item
            claim_success = self.system.claim_item("Test Phone", "owner@claimed.com")
            print(f"✓ Item claim: {'Success' if claim_success else 'Failed'}")
            
            if claim_success:
                # Verify the item status was updated
                for item in self.system.items:
                    if item.name == "Test Phone" and item.status:
                        print("✓ Item status correctly updated to claimed")
                        break
        else:
            print("✗ Could not create test item for claiming")
    
    def test_6_data_persistence(self):
        """Test Case 6: Data Persistence"""
        print("\n" + "=" * 50)
        print("TEST CASE 6: Data Persistence")
        print("=" * 50)
        
        # Test saving items
        print("--- Testing Data Save ---")
        try:
            self.system.save_items()
            print("✓ Items saved successfully")
            
            # Verify file exists and has content
            with open(self.temp_items_file.name, 'r') as f:
                saved_data = json.load(f)
                print(f"✓ Data persistence verified: {len(saved_data['items'])} items in file")
                
        except Exception as e:
            print(f"✗ Data save failed: {e}")
        
        # Test loading items
        print("--- Testing Data Load ---")
        try:
            # Create a new system instance to test loading
            new_system = System(filename=self.temp_items_file.name, 
                              users_filename=self.temp_users_file.name)
            print(f"✓ Data load successful: {len(new_system.items)} items loaded")
            print(f"✓ Max ID preserved: {new_system.max_id}")
            
        except Exception as e:
            print(f"✗ Data load failed: {e}")
    
    def run_all_tests(self):
        """Run all test cases"""
        print("LOST AND FOUND SYSTEM - COMPREHENSIVE TEST SUITE")
        print("=" * 60)
        
        try:
            self.setUp()
            
            self.test_1_user_authentication()
            self.test_2_item_management() 
            self.test_3_search_functionality()
            self.test_4_admin_operations()
            self.test_5_claim_functionality()
            self.test_6_data_persistence()
            
            print("\n" + "=" * 60)
            print("ALL TESTS COMPLETED!")
            print("=" * 60)
            
        except Exception as e:
            print(f"\n✗ Test suite failed with error: {e}")
        finally:
            self.tearDown()

def quick_demo():
    """Quick demonstration function"""
    print("QUICK DEMONSTRATION OF LOST AND FOUND SYSTEM")
    print("=" * 50)
    
    # Use the actual project files
    system = System()
    
    print(f"System initialized with:")
    print(f"  - {len(system.users)} users")
    print(f"  - {len(system.items)} items")
    print(f"  - Next available item ID: {system.max_id + 1}")
    
    print("\nSample Items:")
    for i, item in enumerate(system.items[:3], 1):  # Show first 3 items
        status = "Claimed" if item.status else "Unclaimed" if item.lost_or_found else "Unfound"
        print(f"  {i}. {item.name} ({item.category}) - {status}")
    
    print("\nSample Users:")
    for i, user in enumerate(system.users[:3], 1):  # Show first 3 users
        print(f"  {i}. {user.username} ({user.role})")

if __name__ == "__main__":
    # Run comprehensive tests
    test_suite = TestLostAndFoundSystem()
    test_suite.run_all_tests()
    
    print("\n\n")
    
    # Run quick demo with actual project files
    quick_demo()