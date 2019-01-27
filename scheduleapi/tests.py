from django.test import TestCase
from .models import CouncilRegistration, BinType


class ModelTestCase(TestCase):

    # Council Registration tests
    def test(self):
        """Test for valid Council Registration"""
        obj = CouncilRegistration.objects.create(
            council_id=1,
            council_name='Dave',
            council_code='NT1',
            council_address='1 Tyne Street, North Tyneside'
        )

        self.assertTrue(isinstance(obj, CouncilRegistration))
        self.assertEqual(obj.council_name, 'Dave')
        self.assertEqual(obj.council_code, 'NT1')
        self.assertEqual(obj.council_address, '1 Tyne Street, North Tyneside')

    def test2(self):
        """Test for valid Council Registration"""
        obj = CouncilRegistration.objects.create(
            council_id=2,
            council_name='Steve',
            council_code='ST1',
            council_address='1 South Street, South Tyneside'
        )

        self.assertTrue(isinstance(obj, CouncilRegistration))
        self.assertEqual(obj.council_name, 'Steve')
        self.assertEqual(obj.council_code, 'ST1')
        self.assertEqual(obj.council_address, '1 South Street, South Tyneside')

    def test3_negative(self):
        """Test for valid Council Registration"""
        obj = CouncilRegistration.objects.create(
            council_id=2,
            council_name='Steve',
            council_code='ST1',
            council_address='1 South Street, South Tyneside'
        )

        self.assertFalse(isinstance(obj, BinType))

    def test_recycling(self):
        """Test for valid Bin Type"""
        obj = BinType.objects.create(
            bin_id=1,
            bin_type='Recycling'
        )

        self.assertTrue(isinstance(obj, BinType))
        self.assertEqual(obj.bin_type, 'Recycling')

    def test_recycling_negative(self):
        """Test for valid Bin Type"""
        obj = BinType.objects.create(
            bin_id=1,
            bin_type='Recycling'
        )

        self.assertFalse(isinstance(obj, CouncilRegistration))

    def test_general_waste(self):
        """Test for valid Bin Type"""
        obj = BinType.objects.create(
            bin_id=2,
            bin_type='General Waste'
        )

        self.assertTrue(isinstance(obj, BinType))
        self.assertEqual(obj.bin_type, 'General Waste')

    def test_general_waste_negative(self):
        """Test for valid Bin Type"""
        obj = BinType.objects.create(
            bin_id=2,
            bin_type='General Waste'
        )

        self.assertFalse(isinstance(obj, CouncilRegistration))

    def test_garden_waste(self):
        """Test for valid Bin Type"""
        obj = BinType.objects.create(
            bin_id=3,
            bin_type='Garden Waste'
        )

        self.assertTrue(isinstance(obj, BinType))
        self.assertEqual(obj.bin_type, 'Garden Waste')

    def test_garden_waste_negative(self):
        """Test for valid Bin Type"""
        obj = BinType.objects.create(
            bin_id=3,
            bin_type='Garden Waste'
        )

        self.assertFalse(isinstance(obj, CouncilRegistration))
