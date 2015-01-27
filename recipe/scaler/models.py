# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin.py sqlcustom [app_label]'
# into your database.
from __future__ import unicode_literals

from django.db import models

class Foods(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    name = models.CharField(unique=True, max_length=255)
    name_scientific = models.CharField(max_length=255, blank=True)
    description = models.TextField(blank=True)
    itis_id = models.CharField(max_length=255, blank=True)
    wikipedia_id = models.CharField(max_length=255, blank=True)
    picture_file_name = models.CharField(max_length=255, blank=True)
    picture_content_type = models.CharField(max_length=255, blank=True)
    picture_file_size = models.IntegerField(blank=True, null=True)
    picture_updated_at = models.DateTimeField(blank=True, null=True)
    legacy_id = models.IntegerField(blank=True, null=True)
    food_group = models.CharField(max_length=255, blank=True)
    food_subgroup = models.CharField(max_length=255, blank=True)
    food_type = models.CharField(max_length=255)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    creator_id = models.IntegerField(blank=True, null=True)
    updater_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'foods'


class AccessionNumbers(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    number = models.CharField(max_length=255, blank=True)
    compound_id = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'accession_numbers'


class AuthGroup(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    name = models.CharField(unique=True, max_length=80)

    class Meta:
        managed = True
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    group = models.ForeignKey(AuthGroup)
    permission = models.ForeignKey('AuthPermission')

    class Meta:
        managed = True
        db_table = 'auth_group_permissions'


class AuthPermission(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    name = models.CharField(max_length=50)
    content_type = models.ForeignKey('DjangoContentType')
    codename = models.CharField(max_length=100)

    class Meta:
        managed = True
        db_table = 'auth_permission'


class AuthUser(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField()
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=30)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.CharField(max_length=75)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = True
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    user = models.ForeignKey(AuthUser)
    group = models.ForeignKey(AuthGroup)

    class Meta:
        managed = True
        db_table = 'auth_user_groups'


class AuthUserUserPermissions(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    user = models.ForeignKey(AuthUser)
    permission = models.ForeignKey(AuthPermission)

    class Meta:
        managed = True
        db_table = 'auth_user_user_permissions'


class Classifications(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    compound_id = models.IntegerField(blank=True, null=True)
    compound_classification_id = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'classifications'


class CompoundClassifications(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    name = models.CharField(max_length=255, blank=True)
    code = models.CharField(max_length=255, blank=True)
    type = models.CharField(max_length=255, blank=True)
    ancestry = models.CharField(max_length=255, blank=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'compound_classifications'


class CompoundSynonyms(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    compound_id = models.IntegerField()
    synonym = models.CharField(unique=True, max_length=255)
    source = models.CharField(max_length=255)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'compound_synonyms'


class Compounds(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    legacy_id = models.IntegerField(blank=True, null=True)
    type = models.CharField(max_length=255)
    public_id = models.CharField(unique=True, max_length=9)
    name = models.CharField(unique=True, max_length=255)
    export = models.IntegerField(blank=True, null=True)
    assigned_to_id = models.IntegerField(blank=True, null=True)
    state = models.CharField(max_length=255, blank=True)
    annotation_quality = models.CharField(max_length=255, blank=True)
    description = models.TextField(blank=True)
    cas_number = models.CharField(unique=True, max_length=255, blank=True)
    melting_point = models.TextField(blank=True)
    protein_formula = models.CharField(max_length=255, blank=True)
    protein_weight = models.CharField(max_length=255, blank=True)
    experimental_solubility = models.CharField(max_length=255, blank=True)
    experimental_logp = models.CharField(max_length=255, blank=True)
    hydrophobicity = models.CharField(max_length=255, blank=True)
    isoelectric_point = models.CharField(max_length=255, blank=True)
    metabolism = models.TextField(blank=True)
    kegg_compound_id = models.CharField(unique=True, max_length=255, blank=True)
    pubchem_compound_id = models.CharField(unique=True, max_length=255, blank=True)
    pubchem_substance_id = models.CharField(unique=True, max_length=255, blank=True)
    chebi_id = models.CharField(unique=True, max_length=255, blank=True)
    het_id = models.CharField(max_length=255, blank=True)
    uniprot_id = models.CharField(max_length=255, blank=True)
    uniprot_name = models.CharField(max_length=255, blank=True)
    genbank_id = models.CharField(max_length=255, blank=True)
    wikipedia_id = models.CharField(max_length=255, blank=True)
    synthesis_citations = models.TextField(blank=True)
    general_citations = models.TextField(blank=True)
    comments = models.TextField(blank=True)
    protein_structure_file_name = models.CharField(max_length=255, blank=True)
    protein_structure_content_type = models.CharField(max_length=255, blank=True)
    protein_structure_file_size = models.IntegerField(blank=True, null=True)
    protein_structure_updated_at = models.DateTimeField(blank=True, null=True)
    msds_file_name = models.CharField(max_length=255, blank=True)
    msds_content_type = models.CharField(max_length=255, blank=True)
    msds_file_size = models.IntegerField(blank=True, null=True)
    msds_updated_at = models.DateTimeField(blank=True, null=True)
    mass_spec_file_name = models.CharField(max_length=255, blank=True)
    mass_spec_content_type = models.CharField(max_length=255, blank=True)
    mass_spec_file_size = models.IntegerField(blank=True, null=True)
    mass_spec_updated_at = models.DateTimeField(blank=True, null=True)
    creator_id = models.IntegerField(blank=True, null=True)
    updater_id = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    phenolexplorer_id = models.IntegerField(unique=True, blank=True, null=True)
    dfc_id = models.CharField(unique=True, max_length=255, blank=True)
    hmdb_id = models.CharField(unique=True, max_length=255, blank=True)
    duke_id = models.CharField(max_length=255, blank=True)
    drugbank_id = models.CharField(unique=True, max_length=255, blank=True)
    bigg_id = models.IntegerField(blank=True, null=True)
    eafus_id = models.CharField(unique=True, max_length=255, blank=True)
    knapsack_id = models.CharField(unique=True, max_length=255, blank=True)
    boiling_point = models.CharField(max_length=255, blank=True)
    boiling_point_reference = models.CharField(max_length=255, blank=True)
    charge = models.CharField(max_length=255, blank=True)
    charge_reference = models.CharField(max_length=255, blank=True)
    density = models.CharField(max_length=255, blank=True)
    density_reference = models.CharField(max_length=255, blank=True)
    optical_rotation = models.CharField(max_length=255, blank=True)
    optical_rotation_reference = models.CharField(max_length=255, blank=True)
    percent_composition = models.CharField(max_length=255, blank=True)
    percent_composition_reference = models.CharField(max_length=255, blank=True)
    physical_description = models.TextField(blank=True)
    physical_description_reference = models.TextField(blank=True)
    refractive_index = models.CharField(max_length=255, blank=True)
    refractive_index_reference = models.CharField(max_length=255, blank=True)
    uv_index = models.CharField(max_length=255, blank=True)
    uv_index_reference = models.CharField(max_length=255, blank=True)
    experimental_pka = models.CharField(max_length=255, blank=True)
    experimental_pka_reference = models.CharField(max_length=255, blank=True)
    experimental_solubility_reference = models.CharField(max_length=255, blank=True)
    experimental_logp_reference = models.CharField(max_length=255, blank=True)
    hydrophobicity_reference = models.CharField(max_length=255, blank=True)
    isoelectric_point_reference = models.CharField(max_length=255, blank=True)
    melting_point_reference = models.CharField(max_length=255, blank=True)
    moldb_alogps_logp = models.CharField(max_length=255, blank=True)
    moldb_logp = models.CharField(max_length=255, blank=True)
    moldb_alogps_logs = models.CharField(max_length=255, blank=True)
    moldb_smiles = models.TextField(blank=True)
    moldb_pka = models.CharField(max_length=255, blank=True)
    moldb_formula = models.CharField(max_length=255, blank=True)
    moldb_average_mass = models.CharField(max_length=255, blank=True)
    moldb_inchi = models.TextField(blank=True)
    moldb_mono_mass = models.CharField(max_length=255, blank=True)
    moldb_inchikey = models.CharField(max_length=255, blank=True)
    moldb_alogps_solubility = models.CharField(max_length=255, blank=True)
    moldb_id = models.IntegerField(blank=True, null=True)
    moldb_iupac = models.TextField(blank=True)
    structure_source = models.CharField(max_length=255, blank=True)
    duplicate_id = models.CharField(max_length=255, blank=True)
    old_dfc_id = models.CharField(max_length=255, blank=True)
    dfc_name = models.TextField(blank=True)
    compound_source = models.CharField(max_length=255, blank=True)
    flavornet_id = models.CharField(unique=True, max_length=255, blank=True)
    goodscent_id = models.CharField(unique=True, max_length=255, blank=True)
    superscent_id = models.CharField(unique=True, max_length=255, blank=True)
    phenolexplorer_metabolite_id = models.IntegerField(unique=True, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'compounds'


class CompoundsEnzymes(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    compound_id = models.IntegerField()
    enzyme_id = models.IntegerField()
    citations = models.TextField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    creator_id = models.IntegerField(blank=True, null=True)
    updater_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'compounds_enzymes'


class CompoundsFlavors(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    compound_id = models.IntegerField()
    flavor_id = models.IntegerField()
    citations = models.TextField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    creator_id = models.IntegerField(blank=True, null=True)
    updater_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'compounds_flavors'


class CompoundsFoods(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    compound_id = models.ForeignKey(Compounds, related_name="compounds", db_column='compound_id')
    food_id= models.ForeignKey(Foods, related_name="foods", db_column="food_id")
    orig_food_id = models.CharField(max_length=255, blank=True)
    orig_food_common_name = models.CharField(max_length=255, blank=True)
    orig_food_scientific_name = models.CharField(max_length=255, blank=True)
    orig_food_part = models.CharField(max_length=255, blank=True)
    orig_compound_id = models.CharField(max_length=255, blank=True)
    orig_compound_name = models.CharField(max_length=255, blank=True)
    orig_content = models.DecimalField(max_digits=15, decimal_places=9, blank=True, null=True)
    orig_min = models.DecimalField(max_digits=15, decimal_places=9, blank=True, null=True)
    orig_max = models.DecimalField(max_digits=15, decimal_places=9, blank=True, null=True)
    orig_unit = models.CharField(max_length=255, blank=True)
    orig_citation = models.TextField(blank=True)
    citation = models.TextField()
    citation_type = models.CharField(max_length=255)
    creator_id = models.IntegerField(blank=True, null=True)
    updater_id = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    orig_method = models.CharField(max_length=255, blank=True)
    orig_unit_expression = models.CharField(max_length=255, blank=True)

    class Meta:
        managed = True
        db_table = 'compounds_foods'

    def __unicode__(self):
        return self.orig_compound_name


class CompoundsHealthEffects(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    compound_id = models.IntegerField()
    health_effect_id = models.IntegerField()
    orig_health_effect_name = models.CharField(max_length=255, blank=True)
    orig_compound_name = models.CharField(max_length=255, blank=True)
    orig_citation = models.TextField(blank=True)
    citation = models.TextField()
    citation_type = models.CharField(max_length=255)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    creator_id = models.IntegerField(blank=True, null=True)
    updater_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'compounds_health_effects'


class DjangoAdminLog(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.IntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', blank=True, null=True)
    user = models.ForeignKey(AuthUser)

    class Meta:
        managed = True
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    name = models.CharField(max_length=100)
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = True
        db_table = 'django_content_type'


class DjangoMigrations(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = True
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = True
        db_table = 'django_session'


class EnzymeSynonyms(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    enzyme_id = models.IntegerField()
    synonym = models.CharField(unique=True, max_length=255)
    source = models.CharField(max_length=255)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'enzyme_synonyms'


class Enzymes(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    name = models.CharField(unique=True, max_length=255)
    gene_name = models.CharField(unique=True, max_length=255, blank=True)
    description = models.TextField(blank=True)
    go_classification = models.TextField(blank=True)
    general_function = models.TextField(blank=True)
    specific_function = models.TextField(blank=True)
    pathway = models.TextField(blank=True)
    reaction = models.TextField(blank=True)
    cellular_location = models.CharField(max_length=255, blank=True)
    signals = models.TextField(blank=True)
    transmembrane_regions = models.TextField(blank=True)
    molecular_weight = models.DecimalField(max_digits=15, decimal_places=9, blank=True, null=True)
    theoretical_pi = models.DecimalField(max_digits=15, decimal_places=9, blank=True, null=True)
    locus = models.CharField(max_length=255, blank=True)
    chromosome = models.CharField(max_length=255, blank=True)
    uniprot_name = models.CharField(unique=True, max_length=255, blank=True)
    uniprot_id = models.CharField(unique=True, max_length=100, blank=True)
    pdb_id = models.CharField(unique=True, max_length=10, blank=True)
    genbank_protein_id = models.CharField(unique=True, max_length=20, blank=True)
    genbank_gene_id = models.CharField(unique=True, max_length=20, blank=True)
    genecard_id = models.CharField(unique=True, max_length=20, blank=True)
    genatlas_id = models.CharField(unique=True, max_length=20, blank=True)
    hgnc_id = models.CharField(unique=True, max_length=20, blank=True)
    hprd_id = models.CharField(unique=True, max_length=255, blank=True)
    organism = models.CharField(max_length=255, blank=True)
    general_citations = models.TextField(blank=True)
    comments = models.TextField(blank=True)
    creator_id = models.IntegerField(blank=True, null=True)
    updater_id = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'enzymes'


class Flavors(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    name = models.CharField(unique=True, max_length=255)
    flavor_group = models.CharField(max_length=255, blank=True)
    category = models.CharField(max_length=255, blank=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    creator_id = models.IntegerField(blank=True, null=True)
    updater_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'flavors'





class HealthEffects(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    name = models.CharField(unique=True, max_length=255)
    description = models.TextField(blank=True)
    chebi_name = models.CharField(max_length=255, blank=True)
    chebi_id = models.CharField(max_length=255, blank=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    creator_id = models.IntegerField(blank=True, null=True)
    updater_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'health_effects'


class MapItemsPathways(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    map_item_id = models.IntegerField(blank=True, null=True)
    map_item_type = models.CharField(max_length=255, blank=True)
    pathway_id = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'map_items_pathways'


class Pathways(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    smpdb_id = models.CharField(max_length=255, blank=True)
    kegg_map_id = models.CharField(max_length=255, blank=True)
    name = models.CharField(max_length=255, blank=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'pathways'


class PdbIdentifiers(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    compound_id = models.IntegerField(blank=True, null=True)
    pdb_id = models.CharField(max_length=255, blank=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'pdb_identifiers'


class PfamMemberships(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    enzyme_id = models.IntegerField(blank=True, null=True)
    pfam_id = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'pfam_memberships'


class Pfams(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    identifier = models.CharField(max_length=7, blank=True)
    name = models.CharField(max_length=50, blank=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'pfams'


class Sequences(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    header = models.CharField(max_length=255, blank=True)
    chain = models.TextField(blank=True)
    sequenceable_id = models.IntegerField(blank=True, null=True)
    sequenceable_type = models.CharField(max_length=255, blank=True)
    type = models.CharField(max_length=255, blank=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'sequences'
