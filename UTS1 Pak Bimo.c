#include <stdio.h>
#include <string.h>
#include <stdbool.h>

#define MAX_KARYAWAN 100

typedef struct {
    char nama[50];
    int umur;
    int lamaBekerja;
    char golongan[3];
    int jamKerja;
    float gajiPokok;
    float gajiLembur;
    float bonusLoyalitas;
    float tunjangan;
    float pajakPenghasilan;
} Karyawan;

float hitungGajiPokok(char golongan[]) {
    if (strcmp(golongan, "1A") == 0) return 500000;
    if (strcmp(golongan, "1B") == 0) return 1000000;
    if (strcmp(golongan, "1C") == 0) return 1500000;
    if (strcmp(golongan, "2A") == 0) return 2000000;
    if (strcmp(golongan, "2B") == 0) return 2500000;
    if (strcmp(golongan, "2C") == 0) return 3000000;
    return 0;
}

float hitungTarifLembur(char golongan[]) {
    if (strcmp(golongan, "1A") == 0) return 50000;
    if (strcmp(golongan, "1B") == 0) return 75000;
    if (strcmp(golongan, "1C") == 0) return 100000;
    if (strcmp(golongan, "2A") == 0) return 125000;
    if (strcmp(golongan, "2B") == 0) return 150000;
    if (strcmp(golongan, "2C") == 0) return 175000;
    return 0;
}

float hitungBonusLoyalitas(int lamaBekerja, int umur) {
    if (lamaBekerja >= 7) {
        if (umur >= 55) return 2500000;
        else if (umur < 55) return 2000000;
        else return 1000000;
    }
    return 0;
}

float hitungTunjangan(char golongan[]) {
    char tingkat = golongan[0];
    if (tingkat == '1') return 500000;
    if (tingkat == '2') return 750000;
    return 0;
}

float hitungPajak(float totalPendapatan) {
    if (totalPendapatan <= 5000000) return totalPendapatan * 0.05;
    else if (totalPendapatan <= 10000000) return totalPendapatan * 0.1;
    else return totalPendapatan * 0.15;
}

void tampilkanDetailGaji(Karyawan k) {
    printf("\nDetail Gaji untuk %s:\n", k.nama);
    printf("Gaji Pokok: Rp.%.2f\n", k.gajiPokok);
    printf("Gaji Lembur: Rp.%.2f\n", k.gajiLembur);
    printf("Bonus Loyalitas: Rp.%.2f\n", k.bonusLoyalitas);
    printf("Tunjangan: Rp.%.2f\n", k.tunjangan);
    printf("Pajak Penghasilan: Rp.%.2f\n", k.pajakPenghasilan);
    float totalGaji = k.gajiPokok + k.gajiLembur + k.bonusLoyalitas + k.tunjangan - k.pajakPenghasilan;
    printf("Total Gaji Bersih: Rp.%.2f\n", totalGaji);
}

int main() {
    Karyawan daftarKaryawan[MAX_KARYAWAN];
    int jumlahKaryawan = 0;
    char pilihan;

    do {
        Karyawan k;
        printf("\nMasukkan data karyawan:\n");
        printf("Nama: ");
        scanf("%s", k.nama);
        printf("Umur: ");
        scanf("%d", &k.umur);
        printf("Lama Bekerja (tahun): ");
        scanf("%d", &k.lamaBekerja);
        printf("Golongan (1A/1B/1C/2A/2B/2C): ");
        scanf("%s", k.golongan);
        printf("Jam Kerja: ");
        scanf("%d", &k.jamKerja);

        k.gajiPokok = hitungGajiPokok(k.golongan);
        k.gajiLembur = k.jamKerja > 150 ? (k.jamKerja - 150) * hitungTarifLembur(k.golongan) : 0;
        k.bonusLoyalitas = hitungBonusLoyalitas(k.lamaBekerja, k.umur);
        k.tunjangan = hitungTunjangan(k.golongan);
        float totalPendapatan = k.gajiPokok + k.gajiLembur + k.bonusLoyalitas + k.tunjangan;
        k.pajakPenghasilan = hitungPajak(totalPendapatan);

        daftarKaryawan[jumlahKaryawan++] = k;

        tampilkanDetailGaji(k);

        printf("\nIngin menambah data karyawan lain? (y/n): ");
        scanf(" %c", &pilihan);
    } while (pilihan == 'y' || pilihan == 'Y');

    // Fitur tambahan: Laporan statistik
    float totalGajiPerusahaan = 0;
    int karyawanDenganBonus = 0;
    for (int i = 0; i < jumlahKaryawan; i++) {
        totalGajiPerusahaan += daftarKaryawan[i].gajiPokok + daftarKaryawan[i].gajiLembur + 
                               daftarKaryawan[i].bonusLoyalitas + daftarKaryawan[i].tunjangan - 
                               daftarKaryawan[i].pajakPenghasilan;
        if (daftarKaryawan[i].bonusLoyalitas > 0) karyawanDenganBonus++;
    }

    printf("\n===== Laporan Statistik Perusahaan =====\n");
    printf("Jumlah Karyawan: %d\n", jumlahKaryawan);
    printf("Total Gaji Perusahaan: Rp.%.2f\n", totalGajiPerusahaan);
    printf("Rata-rata Gaji Karyawan: Rp.%.2f\n", totalGajiPerusahaan / jumlahKaryawan);
    printf("Persentase Karyawan dengan Bonus Loyalitas: %.2f%%\n", (float)karyawanDenganBonus / jumlahKaryawan * 100);

    return 0;
}